def serialize(obj):
    if isinstance(obj, dict):
        obj_s = '{'
        for key, value in obj.items():
            key_s = f'{key}'
            value_s = serialize(value)
            obj_s += f'{key_s}:{value_s}'
        obj_s = obj_s[:-1] + '}'
    elif isinstance(obj, str):
        obj_s = f'{obj}'

        return obj_s


def deserialize(string):
    # проверка - словарь
    if string[0] == '{':
        obj = {}
        string = string[1:-1]
        if string:
            key_and_value = string.split(',')
            for key_value in key_and_value:
                key, value = key_value.split(':')
                key = key.strip('')
                obj[key] = deserialize(value)

        return obj

    elif string[0] == '':
        return string[1:-1]

    elif string == 'true':
        return True
    elif string == 'false':
        return False
