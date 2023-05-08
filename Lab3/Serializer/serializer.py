import inspect
import re
from frozendict import frozendict
from types import CodeType, FunctionType
from constants import (CODE_ATTRIBUTE, CLASS_ATTRIBUTE, FUNCTION_ATTRIBUTE,
                        CODE_FIELD, GLOBAL_FIELD, NAME_FIELD, TYPE_FIELD, VALUE_FIELD,
                       CLASS, OBJECT, DICT, FUNC, CODE,
                       PRIMITIVE_TYPES, ITERABLE_TYPES)

"""Class Serializer"""

class Serializer:

    """serialize method"""

    def serialize(self, obj):

        res = {}
        type_ = type(obj)

        if type_ == dict:
            res = self.serialize(obj)
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

    def serialize_type(self):
        pass

    def serialize_itter(self):
        pass

    def serialize_func(self):
        pass

    def serialize_class(self):
        pass

    def serialize_object(self):
        pass

    def serialize_other(self):
        pass

    """deserialize method"""

    def deserialize(self, obj):
        type_string = obj[TYPE_FIELD]
        res = object

        if type_string == DICT:
            res = self.deserialize(obj)
        elif type_string == PRIMITIVE_TYPES:
            res = self.deserialize(obj)
        elif type_string == ITERABLE_TYPES:
            res = self.deserialize(obj)
        elif type_string == FUNC:
            res = self.deserialize(obj)
        elif type_string == CLASS:
            res =self.deserialize(obj)
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

    def deserialize_type(self):
        pass

    def deserialize_itter(self):
        pass

    def deserialize_func(self):
        pass

    def deserialize_class(self):
        pass

    def deserialize_object(self):
        pass

    def deserialize_other(self):
        pass
