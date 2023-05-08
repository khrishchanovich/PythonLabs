import inspect
import re
from frozendict import frozendict
from types import CodeType, FunctionType
from constants import (CODE_ATTRIBUTE, CLASS_ATTRIBUTE, FUNCTION_ATTRIBUTE,
                        CODE_FIELD, GLOBAL_FIELD, NAME_FIELD, TYPE_FIELD, VALUE_FIELD,
                       CLASS, OBJECT, DICT, FUNC, CODE, BASE, DATA,
                       PRIMITIVE_TYPES, ITERABLE_TYPES)

"""Class Serializer"""

class Serializer:

    """serialize method"""

    def serialize(self, obj):

        res = {}
        type_ = type(obj)

        if type_ == dict:
            res = self.serialize_dict(obj)

        elif type_ == list:
            res = self.serialize(obj)

        elif type_ == tuple:
            res = self.serialize(obj)

        elif type_ == set:
            res = self.serialize(obj)

        elif isinstance(obj, (int, float, complex, bool, str, type(None))):
            res = self.serialize(obj)

        elif inspect.isfunction(obj):
            res = self.serialize(obj)

        elif inspect.ismethod(obj):
            res = self.serialize(obj)

        elif inspect.iscode(obj):
            res = self.serialize(obj)

        elif hasattr(obj, '__dict__'):
            res = self.serialize(obj)

        return tuple(res)

    def serialize_dict(self, obj: dict):
        res = {VALUE_FIELD: {}}

        for key, value in obj.items():
            res_key = self.serialize(key)
            res_value = self.serialize(value)

            res[VALUE_FIELD][res_key] = res_value

        return res

    def serialize_primitive(self, obj):
        res = {VALUE_FIELD: str(obj)}

        return res

    def serialize_itter(self, obj):
        res = {VALUE_FIELD: []}

        for value in obj:
            res[VALUE_FIELD].append(self.serialize(value))

        res[VALUE_FIELD] = tuple(res[VALUE_FIELD])

        return res

    def serialize_func(self):
        pass

    def serialize_class(self, obj):
        res = {VALUE_FIELD: {}}

        members = []
        bases = []

        for base in obj.__bases__:
            if base.__name__ != OBJECT:
                bases.append(base)

        res[VALUE_FIELD][self.serialize(BASE)] = self.serialize(bases)

        for member in inspect.getmembers(obj):
            if member[0] not in CLASS_ATTRIBUTE:
                members.append(member)

        res_data = self.serialize(DATA)

        dict_ = {NAME_FIELD: obj.__name__}

        for member in members:
            dict_[member[0]] = member[1]

        res[VALUE_FIELD][res_data] = self.serialize(dict_)

        return res


    def serialize_object(self, obj):
        res = {VALUE_FIELD: {}}
        type_ = type(obj)

        for attr, value in obj.__dict__.items():
            res_attr = self.serialize(attr)
            res_value = self.serialize(value)

            res[VALUE_FIELD][res_attr] = res_value

        res[VALUE_FIELD][self.serialize(TYPE_FIELD)] = self.serialize(type_)

        return res

    def serialize_other(self):
        pass

    """deserialize method"""

    def deserialize(self, obj):
        type_string = obj[TYPE_FIELD]
        res = object

        if type_string == DICT:
            res = self.deserialize_dict(obj)

        elif type_string == PRIMITIVE_TYPES:
            res = self.deserialize(obj)

        elif type_string == ITERABLE_TYPES:
            res = self.deserialize(obj)

        elif type_string == FUNC:
            res = self.deserialize(obj)

        elif type_string == CLASS:
            res = self.deserialize(obj)

        elif type_string == OBJECT:
            res = self.deserialize(obj)

        return res

    def deserialize_dict(self, obj):
        res = {}

        if type(obj[VALUE_FIELD]) == tuple:
            return {}

        for key, value in obj[VALUE_FIELD].items():
            res_key = self.deserialize(key)
            res_value = self.deserialize(value)

            res[res_key] = res_value

        return res

    def deserialize_primitive(self, obj):
        res = obj

        if obj[TYPE_FIELD] == PRIMITIVE_TYPES[0]:
            res = int(obj[VALUE_FIELD])

        elif obj[TYPE_FIELD] == PRIMITIVE_TYPES[1]:
            res = float(obj[VALUE_FIELD])

        elif obj[TYPE_FIELD] == PRIMITIVE_TYPES[2]:
            res = complex(obj[VALUE_FIELD])

        elif obj[TYPE_FIELD] == PRIMITIVE_TYPES[3]:
            res = bool(obj[VALUE_FIELD])

        elif obj[TYPE_FIELD] == PRIMITIVE_TYPES[4]:
            res = obj[VALUE_FIELD]

        elif obj[TYPE_FIELD] == PRIMITIVE_TYPES[5]:
            res = None

        return res

    def deserialize_itter(self, obj):
        res = []

        for value in obj[VALUE_FIELD]:
            res_value = self.deserialize(value)
            res.append(res_value)

        if obj[TYPE_FIELD] == ITERABLE_TYPES[0]:
            res = list(res)

        elif obj[TYPE_FIELD] == ITERABLE_TYPES[1]:
            res = tuple(res)

        elif obj[TYPE_FIELD] == ITERABLE_TYPES[2]:
            res = bytes(res)

        elif obj[TYPE_FIELD] == ITERABLE_TYPES[3]:
            res = set(res)

        return res

    def deserialize_func(self):
        pass

    def deserialize_class(self, obj):
        res_data = self.serialize(DATA)

        res_bases = tuple(self.deserialize(obj[VALUE_FIELD][self.serialize(BASE)]))

        res = self.deserialize(obj[VALUE_FIELD][res_data])
        res_name = res[NAME_FIELD]

        del res[NAME_FIELD]

        return type(res_name, (object,), res)

    def deserialize_object(self, obj):
        res = object

        res = self.deserialize(obj[VALUE_FIELD][self.deserialize(TYPE_FIELD)])

        for attr, value in obj[VALUE_FIELD].items():
            res_attr = self.deserialize(attr)
            res_value = self.deserialize(value)

            res.res_attr = res_value

        return res

    def deserialize_other(self):
        pass
