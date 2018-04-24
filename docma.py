""" Document and validate schemas in one easy place

    * Licensed under terms of MIT license (see LICENSE-MIT)
    * Copyright (c) 2018 Neil Joshi

"""

__all__ = ['docma']
__version__ = '0.1.0'


class Docma(object):
    @staticmethod
    def type_to_string(type):
        if type == "int":
            return int
        elif type == "str":
            return str
        elif type == "boolean":
            return bool

    @staticmethod
    def parse_prop(prop_str):
        if ':' in prop_str:
            name, type = prop_str.split(':')
            return name.strip().lower(), lambda prop: isinstance(prop, Docma.type_to_string(type.strip().lower()))

    @staticmethod
    def parse(doc):
        fields = doc.split('\n')
        return dict([validator for validator in map(Docma.parse_prop, fields) if validator is not None])

    def __init__(self):
        self._props = Docma.parse(self.__doc__)

    def __setattr__(self, key, value):
        if key != "_props":
            if key in self._props and not self._props[key](value):
                raise AttributeError("invalid format for {}".format(key))
        self.__dict__[key] = value
