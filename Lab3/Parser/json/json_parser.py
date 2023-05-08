from json import serialize_json, deserialize_json
from Lab3.Parser.parser import Parser


class Json(Parser):

    def dump(self, obj, file):
        with open(file, 'w') as f:
            f.write(self.dumps(obj))

    def dumps(self, obj) -> str:
        obj_ = self.serializer.serialize(obj)
        return serialize_json(obj_)

    def load(self, file):
        with open(file, 'r') as f:
            return self.loads(f.read())

    def loads(self, str_):
        obj_ = self.serializer.deserialize(deserialize_json(str_))
        return obj_


if __name__ == "__main__":
    str_ = {"name":"Luci"}

    with open('JSON.json', 'w') as f:
        Json.dump(str_, f)
