from Lab3.Parser.parser import Parser
from Lab3.Parser.xml.xml import *


class Xml(Parser):
    def dump(self, obj, file):
        with open(file, 'w+') as f:
            f.write(self.dumps(obj))

    def dumps(self, obj):
        obj_ = self.serializer.serialize(obj)
        return serialize_xml(obj_)

    def load(self, file):
        with open(file, 'r') as f:
            return self.loads(f.read())

    def loads(self, string):
        return self.serializer.deserialize(deserialize_xml(string))
