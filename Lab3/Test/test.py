import unittest
from Lab3.Serializer.serializer import Serializer
from Lab3.Parser.json.json_parser import Json
from Lab3.Test.constants import JSON_PATH, DATA_DIR
import os
from Lab3.Factory.factory import Factory
from test_data import int_, float_, complex_, bool_, str_, none_

class JSONPrimitiveTypesCase(unittest.TestCase):
    json_serializer = Json()

    def test_dumps_only(self):
        self.assertEqual(self.json_serializer.dumps('123'), '{"VALUE": "123", "TYPE": "str"}')
        self.assertEqual(self.json_serializer.dumps(123), '{"VALUE": "123", "TYPE": "int"}')
        self.assertEqual(self.json_serializer.dumps(123.123), '{"VALUE": "123.123", "TYPE": "float"}')
        self.assertEqual(self.json_serializer.dumps(123j + 0.123), '{"VALUE": "(0.123+123j)", "TYPE": "complex"}')
        self.assertEqual(self.json_serializer.dumps('False'), '{"VALUE": "False", "TYPE": "str"}')
        self.assertEqual(self.json_serializer.dumps(True), '{"VALUE": "True", "TYPE": "bool"}')
        self.assertEqual(self.json_serializer.dumps(''), '{"VALUE": "", "TYPE": "str"}')

    def test_loads_only(self):
        self.assertEqual(self.json_serializer.loads('{"VALUE": "123", "TYPE": "str"}'), '123')
        self.assertEqual(self.json_serializer.loads('{"VALUE": "123", "TYPE": "int"}'), 123)
        self.assertEqual(self.json_serializer.loads('{"VALUE": "123.123", "TYPE": "float"}'), 123.123)
        self.assertEqual(self.json_serializer.loads('{"VALUE": "(0.123+123j)", "TYPE": "complex"}'), 123j + 0.123)
        self.assertEqual(self.json_serializer.loads('{"VALUE": "False", "TYPE": "str"}'), 'False')
        self.assertEqual(self.json_serializer.loads('{"VALUE": "True", "TYPE": "bool"}'), True)
        self.assertEqual(self.json_serializer.loads('{"VALUE": "", "TYPE": "str"}'), '')

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

