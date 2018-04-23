## Docma
Describing schemas in docstrings

# Basic Example
```
class Person(Docma):
    """
    name: str
    age: int
    is_happy: boolean [default: True]
    """
    
    def do_stuff():
        ...

>>> me = Person()
>>> me.name = "Kimba Futu"
>>> me.age = "20"
Raise: ValueError ('age' must be a valid int)
>>> me.age = 20
>>> print(me.is_happy)
True

>>> you = Person.from_dict({'name': 'Owasu Pokuti', 'age': '67', 'is_happy': True})
Raise: ValueError('age' msut be a valid int)
>>> you = Person.from_dict({'name': 'Owasu Pokuti', 'age': 67, 'is_happy': True})
>>>
```