import unittest

from Lab3.Parser.json.json_parser import Json
from Lab3.Parser.xml.xml_parser import Xml


class JSONPrimitiveTypesCase(unittest.TestCase):
    json_serializer = Json()
    xml_serializer = Xml()

    def test_dumps_only(self):
        self.assertEqual(self.json_serializer.dumps('123'), '{"VALUE": "123", "TYPE": "str"}')
        self.assertEqual(self.xml_serializer.dumps('123'), '')

        self.assertEqual(self.json_serializer.dumps(123), '{"VALUE": "123", "TYPE": "int"}')
        self.assertEqual(self.json_serializer.dumps(123.123), '{"VALUE": "123.123", "TYPE": "float"}')
        self.assertEqual(self.json_serializer.dumps(123j + 0.123), '{"VALUE": "(0.123+123j)", "TYPE": "complex"}')
        self.assertEqual(self.json_serializer.dumps('False'), '{"VALUE": "False", "TYPE": "str"}')
        self.assertEqual(self.json_serializer.dumps(False), '{"VALUE": "False", "TYPE": "bool"}')
        self.assertEqual(self.json_serializer.dumps(''), '{"VALUE": "", "TYPE": "str"}')
        self.assertEqual(self.json_serializer.dumps(None), '{"VALUE": "None", "TYPE": "NoneType"}')

    def test_loads_only(self):
        self.assertEqual(self.json_serializer.loads('{"VALUE": "123", "TYPE": "str"}'), '123')
        self.assertEqual(self.json_serializer.loads('{"VALUE": "123", "TYPE": "int"}'), 123)
        self.assertEqual(self.json_serializer.loads('{"VALUE": "123.123", "TYPE": "float"}'), 123.123)
        self.assertEqual(self.json_serializer.loads('{"VALUE": "(0.123+123j)", "TYPE": "complex"}'), 123j + 0.123)
        self.assertEqual(self.json_serializer.loads('{"VALUE": "False", "TYPE": "str"}'), 'False')
        self.assertEqual(self.json_serializer.loads('{"VALUE": "True", "TYPE": "bool"}'), True)
        self.assertEqual(self.json_serializer.loads('{"VALUE": "", "TYPE": "str"}'), '')
        self.assertEqual(self.json_serializer.loads('{"VALUE": "None", "TYPE": "NoneType"}'), None)

    def test_dumps_and_loads(self):
        self.assertEqual(self.json_serializer.dumps('123'), '{"VALUE": "123", "TYPE": "str"}')
        self.assertEqual(self.json_serializer.loads('{"VALUE": "123", "TYPE": "str"}'), '123')

        self.assertEqual(self.json_serializer.dumps(123), '{"VALUE": "123", "TYPE": "int"}')
        self.assertEqual(self.json_serializer.loads('{"VALUE": "123", "TYPE": "int"}'), 123)

        self.assertEqual(self.json_serializer.dumps(123.123), '{"VALUE": "123.123", "TYPE": "float"}')
        self.assertEqual(self.json_serializer.loads('{"VALUE": "123.123", "TYPE": "float"}'), 123.123)

        self.assertEqual(self.json_serializer.dumps(123j + 0.123), '{"VALUE": "(0.123+123j)", "TYPE": "complex"}')
        self.assertEqual(self.json_serializer.loads('{"VALUE": "(0.123+123j)", "TYPE": "complex"}'), 123j + 0.123)

        self.assertEqual(self.json_serializer.dumps('False'), '{"VALUE": "False", "TYPE": "str"}')
        self.assertEqual(self.json_serializer.loads('{"VALUE": "False", "TYPE": "str"}'), 'False')

        self.assertEqual(self.json_serializer.dumps(True), '{"VALUE": "True", "TYPE": "bool"}')
        self.assertEqual(self.json_serializer.loads('{"VALUE": "True", "TYPE": "bool"}'), True)

        self.assertEqual(self.json_serializer.dumps(''), '{"VALUE": "", "TYPE": "str"}')
        self.assertEqual(self.json_serializer.loads('{"VALUE": "", "TYPE": "str"}'), '')

    def test_dump_and_load(self):
        """***"""
        with open('Files/JSON.json', 'w+') as file:
            self.json_serializer.dump('123', 'Files/JSON.json')

        with open('Files/JSON.json', 'r') as file:
            self.assertEqual(self.json_serializer.load('Files/JSON.json'), '123')
        """***"""

        """***"""
        with open('Files/JSON.json', 'w+') as file:
            self.json_serializer.dump(123, 'Files/JSON.json')

        with open('Files/JSON.json', 'r') as file:
            self.assertEqual(self.json_serializer.load('Files/JSON.json'), 123)
        """***"""

        """***"""
        with open('Files/JSON.json', 'w+') as file:
            self.json_serializer.dump(123.123, 'Files/JSON.json')

        with open('Files/JSON.json', 'r') as file:
            self.assertEqual(self.json_serializer.load('Files/JSON.json'), 123.123)
        """***"""

        """***"""
        with open('Files/JSON.json', 'w+') as file:
            self.json_serializer.dump(123j + 0.123, 'Files/JSON.json')

        with open('Files/JSON.json', 'r') as file:
            self.assertEqual(self.json_serializer.load('Files/JSON.json'), 123j + 0.123)
        """***"""

        """***"""
        with open('Files/JSON.json', 'w+') as file:
            self.json_serializer.dump('False', 'Files/JSON.json')

        with open('Files/JSON.json', 'r') as file:
            self.assertEqual(self.json_serializer.load('Files/JSON.json'), 'False')
        """***"""

        """***"""
        with open('Files/JSON.json', 'w+') as file:
            self.json_serializer.dump(True, 'Files/JSON.json')

        with open('Files/JSON.json', 'r') as file:
            self.assertEqual(self.json_serializer.load('Files/JSON.json'), True)
        """***"""

        """***"""
        with open('Files/JSON.json', 'w+') as file:
            self.json_serializer.dump('', 'Files/JSON.json')

        with open('Files/JSON.json', 'r') as file:
            self.assertEqual(self.json_serializer.load('Files/JSON.json'), '')
        """***"""

        with open('Files/JSON.json', 'w+') as file:
            self.json_serializer.dump('', 'Files/JSON.json')

        with open('Files/JSON.json', 'r') as file:
            self.assertEqual(self.json_serializer.load('Files/JSON.json'), '')


class JSONCollectionsCase(unittest.TestCase):
    json_serialize = Json()

    def test_empty(self):
        self.assertEqual(self.json_serialize.loads(self.json_serialize.dumps({})), {})
        self.assertEqual(self.json_serialize.loads(self.json_serialize.dumps(())), ())
        self.assertEqual(self.json_serialize.loads(self.json_serialize.dumps([])), [])
        self.assertEqual(self.json_serialize.loads(self.json_serialize.dumps(set())), set())

    def test_single_value(self):
        self.assertEqual(self.json_serialize.loads(self.json_serialize.dumps({None: 0})), {None: 0})
        self.assertEqual(self.json_serialize.loads(self.json_serialize.dumps(([None]))), ([None]))
        self.assertEqual(self.json_serialize.loads(self.json_serialize.dumps([None])), [None])
        self.assertEqual(self.json_serialize.loads(self.json_serialize.dumps({None})), {None})

    def test_longer_object(self):
        test_1 = {
            1: 2,
            '3': [4, -5, -6, "something {([smth])} '''something"],
            7: {
                6: '8',
                9: {
                    10: None,
                    'None': (True, False)
                }
            }
        }
        self.assertEqual(self.json_serialize.loads(self.json_serialize.dumps(test_1)), test_1)


class TestClass1:
    PROP1 = {
        'a': None,
        'b': True,
        'c': False
    }

    def __init__(self, aa):
        self.a = 4
        self.aa = aa

    def test_bound_1(self):
        return self.a + self.aa

    @staticmethod
    def test_static_1(a):
        return a * 3


class TestClass2(TestClass1):
    PROP2 = 'abc1 def@ ghi'

    def __init__(self, bb):
        super().__init__(bb * 2)
        self.b = 5
        self.bb = bb - 0.8

    @classmethod
    def test_class_2(cls):
        return cls.PROP1


class ClassCase(unittest.TestCase):
    json_serializer = Json()

    def test_no_inheritance(self):
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(TestClass1(12).test_bound_1())),
                         TestClass1(12).test_bound_1())
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(TestClass1.test_static_1(2))),
                         TestClass1.test_static_1(2))

    def test_single_class_inheritance(self):
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(TestClass2.PROP1)), TestClass2.PROP1)
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(TestClass2(12).test_bound_1())),
                         TestClass2(12).test_bound_1())
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(TestClass2.test_class_2())),
                         TestClass2.test_class_2())


GLOBAL_VAL = 20


def test_func():
    return 3


def test_func_1(x):
    return x + 2


def test_func_2(x, y):
    return (GLOBAL_VAL / (x ** 2 + 1)) + 2 * y


def test_func_3(x, y, operation):
    a = operation(x * operation(y)) + GLOBAL_VAL

    def inner_test_func_3(b):
        return (x + b) / (y + a)

    return inner_test_func_3(y / x)


def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


class FuncCase(unittest.TestCase):
    json_serializer = Json()

    def test_zero_arg(self):
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(test_func())), test_func())

    def test_one_arg(self):
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(test_func_1(0))), test_func_1(0))

    def test_globals(self):
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(test_func_2(12, -3))),
                         test_func_2(12, -3))

    def test_closures(self):
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(test_func_3(2, -3, lambda x: x**2))),
                         test_func_3(2, -3, lambda x: x**2))

    def test_recursions(self):
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(factorial(5))), factorial(5))


if __name__ == "__main__":
    unittest.main()