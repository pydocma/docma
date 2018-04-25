## Docma
Describing schemas in docstrings

## Status
[![Build Status](https://travis-ci.org/pydocma/docma.svg?branch=master)](https://travis-ci.org/pydocma/docma)

# Basic Example
```
class Person(Docma):
    """
    name: str
    age: int
    is_happy: boolean
    """
    
    def do_stuff():
        ...

>>> me = Person()
>>> me.name = "Kimba Futu"
>>> me.age = "20"
Raise: ValueError ('age' must be a valid int)
>>> me.age = 20
>>> print(me.is_happy)
False

>>> you = Person.from_dict({'name': 'Owasu Pokuti', 'age': '67', 'is_happy': True})
Raise: ValueError('age' msut be a valid int)
>>> you = Person.from_dict({'name': 'Owasu Pokuti', 'age': 67, 'is_happy': True})
>>>
```
