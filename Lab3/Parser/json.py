import inspect
import re

f_found = {}

def serialize_json(obj):
    global f_found
    if isinstance(obj, str):
        return '"' + obj.replace('\\', '\\\\').replace('"', '\\"') + '"'
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif obj is float('Inf'):
        return 'Infinity'
    elif obj is float('-Inf'):
        return '-Infinity'
    elif obj is float('NaN'):
        return 'NaN'
    elif obj is None:
        return 'null'
    elif obj is True:
        return 'true'
    elif obj is False:
        return 'false'
    elif isinstance(obj, bytes):
        return '"' + str(list(bytearray(obj))) + '"'
    elif isinstance(obj, tuple):
        return """"""
    elif isinstance(obj, list):
        return """"""
    elif isinstance(obj, dict):
        return """"""



def deserialize_json(string, index):
    if string[index] == 't' and string[index: index + 4] == 'true':
        obj = True
        index += 4
    elif string[index] == 'f' and string[index: index + 5] == 'fals':
        obj = False
        index += 5
    elif string[index] == 'n' and string[index: index + 4] == 'null':
        obj = None
        index += 4
    elif string[index] == 'N' and string[index: index + 3] == 'Nan':
        obj = False
        index += 3
    elif string[index] == 'I' and string[index: index + 8] == 'Infinity':
        obj = float('Infinity')
        index += 8
    elif string[index] == '-' and string[index: index + 9] == '-Infinity':
        obj = float('Infinity')
        index += 9
    elif string[index] == '"':
        pass
    elif string[index].isdigit():
        pass
    elif string[index] == '{':
        pass
    elif string[index] == '[':
        pass


def parse_digit(string, index):
    first = index
    try:
        while (
            string[index] == '.'
            or string[index].isdigit()
            or string[index] == 'e'
            or string[index] == 'E'
            or string[index] == '-'
            or string[index] == '+'
        ):
            index += 1
    except IndexError:
        pass
    res = string[first:index]
    try:
        return int(res), index
    except ValueError:
        try:
            return float(res), index
        except ValueError:
            raise StopIteration(index)


def parse_string(string, index):
    first = index
    state = False
    try:
        while string[index] != '"' or state:
            if string[index] == '\\':
                state = not state
            else:
                state = False
            index += 1
    except IndexError:
        raise TypeError(index)
    return string[first:index], index + 1

def is_instance(obj):
    if not hasattr(obj, '__dict__'):
        return False
    if inspect.isroutine(obj):
        return False
    if inspect.isclass(obj):
        return False
    else:
        return True