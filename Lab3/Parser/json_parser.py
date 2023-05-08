from json import serialize, deserialize


def dumps(obj) -> str:
    obj = serialize(obj)
    return obj


def dump(obj, file):
    file.write(dumps(obj))


def loads(obj: str):
    return deserialize(obj).replace('\\n', '\n')


def load(file):
    return loads(file.read)


if __name__ == "__main__":
    str_ = {"name":"Luci"}
    with open('f.json', 'w') as f:
        dump(str_, f)
