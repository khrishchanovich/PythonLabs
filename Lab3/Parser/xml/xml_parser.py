from Lab3.Parser.parser import Parser
from Lab3.Parser.xml.xml import from_string_objects, to_string_objects, from_dict, to_dict


class Xml(Parser):
    def dump(self, obj, file):
        with open(file, 'w+') as f:
            f.write(str(self.dumps(obj)))

    def dumps(self, obj):
        obj_ = to_dict(obj)
        return from_dict(to_string_objects(obj_))

    def load(self, file):
        with open(file, 'r') as f:
            return self.loads(eval(f.read()))

    def loads(self, string):
        obj_ = from_dict(to_dict(string))
        return from_string_objects(obj_)
