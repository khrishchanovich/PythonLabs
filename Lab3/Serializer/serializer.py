import inspect
import re
import pickle

"""Class Serializer"""


class Serializer:

    @staticmethod
    def serializer(obj):

        data_ = {}
        type_ = type(obj)

        """
        list []
        tuple ()
        dict {k:v}
        set {k}
        """

        if type_ == list:
            data_['type'] = 'list'
            data_['value'] = tuple([Serializer.serializer(i) for i in obj])
        elif type_ == tuple:
            data_['type'] = 'tuple'
            data_['value'] = tuple([Serializer.serializer(i) for i in obj])
        elif type_ == set:
            data_['type'] = 'set'
            data_['value'] = tuple(Serializer.serializer(i) for i in obj)
        elif type_ == dict:
            data_['type'] = 'dict'
            data_['value'] = {}
            for i in obj:
                key = Serializer.serializer(i)
                value = Serializer.serializer(obj[i])
                data_['value'][key] = value
            data_['value'] = tuple((k, data_['value'][k]) for k in data_['value'])

        """
        
        """
        return data_

    def deserializer(self, obj):
        pass
