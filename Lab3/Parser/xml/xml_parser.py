from Lab3.Parser.parser import Parser
from Lab3.Parser.xml.xml import from_string_objects, to_string_objects


class Xml(Parser):
    def dump(self, obj, file):
        with open(file, 'w+') as f:
            f.write(self.dumps(obj))

    def dumps(self, obj):
        obj_ = self.serializer.serialize(obj)
        return to_string_objects(obj_)

    def load(self, file):
        with open(file, 'r') as f:
            return self.loads(f.read())

    def loads(self, string):
        return from_string_objects((self.serializer.deserialize(string)))
