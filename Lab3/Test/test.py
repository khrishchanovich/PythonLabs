import unittest
from Lab3.Serializer.serializer import Serializer
from Lab3.Parser.json.json_parser import Json
from Lab3.Test.constants import JSON_PATH
from Lab3.Factory.factory import Factory
from test_data import int_, float_, complex_, bool_, str_, none_


class JSONPrimitiveTypesCase(unittest.TestCase):
    json_serializer = Json()

    def test_dumps_only(self):
        self.assertEqual(self.json_serializer.dumps('123'), '{"VALUE": "123", "TYPE": "str"}')
        self.assertEqual(self.json_serializer.dumps(123), '{"VALUE": "123", "TYPE": "int"}')
        self.assertEqual(self.json_serializer.dumps(123.123), '{"VALUE": "123.123", "TYPE": "float"}')
        self.assertEqual(self.json_serializer.dumps(123j + 0.123), '{"VALUE": "(0.123+123j)", "TYPE": "complex"}')
        self.assertEqual(self.json_serializer.dumps("False"), '{"VALUE": "False", "TYPE": "str"}')
        self.assertEqual(self.json_serializer.dumps(True), '{"VALUE": "True", "TYPE": "bool"}')
        self.assertEqual(self.json_serializer.dumps(""), '{"VALUE": "", "TYPE": "str"}')

    def test_loads_only(self):
        self.assertEqual(self.json_serializer.loads('{"VALUE": "", "TYPE": "str"}'), '')
