from Lab3.Parser.parser import Parser
from Lab3.Parser.xml.xml import from_string_objects, to_string_objects, from_dict, to_dict
from json import dump

class Xml(Parser):
    def dump(self, obj, file):
        with open(file, 'w+') as f:
            f.write(self.dumps(obj))

    def dumps(self, obj):
        return to_dict(to_string_objects(obj))

    def load(self, file):
        with open(file, 'r') as f:
            return self.loads(file)

    def loads(self, string):
        return from_dict(from_string_objects(string))
