import inspect
import re


class Serializer:

    def serializer(self, obj):
        object_ = {}
        type_ = type(obj)
        if type_ == list:
            object_['type'] = 'list'
            object_['value'] = []

            """tuple([])"""

        elif type_ == dict:
            object_['type'] = 'dict'
            object_['value'] = {}

            """keys and values -> tuple()"""

        elif type_ == tuple:
            object_['type'] = 'tuple'
            object_['value'] = tuple()
        elif type_ == set:
            object_['type'] = 'set'
            object_['value'] = {}

            """keys ->  tuple"""

        elif isinstance(obj, (int, float, str, bool)):
            pass
        elif inspect.isroutine(obj):
            pass
        elif obj is None:
            pass


    def deserializer(self, obj):
        pass