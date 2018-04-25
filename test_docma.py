from __future__ import with_statement

from pytest import raises

from docma import Docma


def test_simple():
    class TestSimple(Docma):
        """
        field1: str
        field2: int
        field3: boolean
        """
        pass

    t1 = TestSimple()
    t1.field1 = "foo"
    t1.field4 = "unknown"
    assert t1.field1 == "foo"

    with raises(AttributeError):
        t1.field2 = "12"

    t1.field2 = 12
    assert t1.field2 == 12

    t1.field3 = True
    assert t1.field3


def test_from_dict():
    class TestSimple(Docma):
        """
        field1: str
        field2: int
        field3: boolean
        """
        pass

    t1 = TestSimple.from_dict({
        "field1": "foo",
        "field2": 12,
        "field3": True
    })
    t1.field1 = "foo"
    assert t1.field1 == "foo"

    t1.field2 = 12
    assert t1.field2 == 12

    assert t1.field3


def disabled_test_default():
    class TestSimple(Docma):
        """
        field1: str
        field2: int
            default: 10
        field3: boolean
        """
        pass

    t1 = TestSimple()
    t1.field1 = "foo"
    t1.field3 = True

    assert t1.field1 == "foo"
    assert t1.field2 == 10
    assert t1.field3


def disabled_test_custom_validator():
    class TestSimple(Docma):
        """
        field1: str
            validator: [a-z]+
        field2: int
            default: 10
        field3: boolean
        """
        pass

    t1 = TestSimple()
    t1.field3 = True

    with raises(AttributeError):
        t1.field1 = "Foo"

    t1.field1 = "foo"
    assert t1.field1 == "foo"
    assert t1.field2 == 10
    assert t1.field3


def disabled_test_list_validator():
    class TestSimple(Docma):
        """
        field1: list(str)
            validator: [a-z]+
        field2: list(int)
            default: [10]
        field3: list(boolean)
        """
        pass

    t1 = TestSimple()
    t1.field3 = [True, True]

    with raises(AttributeError):
        t1.field1 = ["Foo"]

    t1.field1 = ["foo"]
    assert t1.field1 == ["foo"]
    assert t1.field2 == [10]
    assert all(t1.field3)


def disabled_test_custom_types():
    class TestSimple(Docma):
        """
        field1: str
            validator: [a-z]+
        field2: int
            default: 10
        field3: boolean
        """
        pass

    class TestSimple2(Docma):
        """
        field1: TestSimple
        """
        pass

    t2 = TestSimple2.from_dict({
        "field1": {
            "field1": "foo",
            "field2": 12,
            "field3": True
        }
    })

    assert t2.field1.field2 == 12
