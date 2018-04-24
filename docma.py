""" Document and validate schemas in one easy place

    * Licensed under terms of MIT license (see LICENSE-MIT)
    * Copyright (c) 2018 Neil Joshi

"""

__all__ = ['docma']
__version__ = '0.1.0'

__supported_types__ = {
    "str": str,
    "int": int,
    "boolean": bool,
    "float": float
}


def parse_prop(prop_str):
    if ':' in prop_str:
        name, type = prop_str.split(':')
        name = name.strip().lower()
        type = type.strip().lower()
        return name, lambda prop: isinstance(prop, __supported_types__[type])


def parse(doc):
    fields = doc.split('\n')
    return dict([validator for validator in map(parse_prop, fields) if validator is not None])


class Docma(object):
    def __init__(self):
        self._props = parse(self.__doc__)

    @classmethod
    def from_dict(cls, dict):
        c = cls()
        for key, value in dict.items():
            c.__setattr__(key, value)
        return c

    def __setattr__(self, key, value):
        if key != "_props":
            if key in self._props and not self._props[key](value):
                raise AttributeError("invalid format for {}".format(key))
        self.__dict__[key] = value
