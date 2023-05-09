import builtins
import inspect
from types import LambdaType, CodeType, FunctionType

from Lab3.Parser.xml.constants import PRIMITIVE_TYPES

def to_string(data, tag):
    item = '<' + tag + '>'
    for key, value in data.items():
        if isinstance(value, dict):
            item += to_string(key, value)
        else:
            item += '<' + key + '>' + str(value) + '</' + key + '>'
    item += '</' + tag + '>'

    return item


def from_string_objects(obj):
    if isinstance(obj, PRIMITIVE_TYPES):
        return obj

    elif isinstance(obj, (list, tuple, set, dict)):
        return obj

    elif inspect.isfunction(obj) or inspect.ismethod(obj) or isinstance(obj, LambdaType):
        return obj

    elif inspect.isclass(obj):
        return obj

    elif inspect.iscode(obj):
        return obj

    elif getattr(obj, "__iter__", None) is not None:
        return obj

    else:
        return obj

def to_string_objects(src):
    if isinstance(src, PRIMITIVE_TYPES):
        return src

    elif isinstance(src, dict):
        if 'function' is src.values():
            return from_string_func(src)

        elif 'object' in src.values():
            return from_string_object(src)

        elif 'class' in src.values():
            return from_string_class(src)

        else:
            return from_string_itter(src)

    elif getattr(src, "__iter__", None) is not None:
        return from_string_itter(src)

    else:
        raise Exception('Unknown type')

def from_string_func(src):
    arg = src['__arg__']
    globs = src['__globals__']

    globs['__builtins__'] = builtins

    for key in src['__globals__']:
        if key in arg['co_names']:
            try:
                globs[key] = __import__(src['__globals__'][key])
            except:
                if globs[key] != src['__name__']:
                    globs[key] = to_string_objects(src['__globals__'][key])

    code_arg = CodeType(arg['co_argcount'],
                        arg['co_code'],
                        arg['co_cellvars'],
                        arg['co_consts'],
                        arg['co_filename'],
                        arg['co_firstlineno'],
                        arg['co_flags'],
                        arg['co_lnotab'],
                        arg['co_freevars'],
                        arg['co_posonlyargcount'],
                        arg['co_kwonlyargcount'],
                        arg['co_name'],
                        arg['co_qualname'],
                        arg['co_names'],
                        arg['co_nlocals'],
                        arg['co_stacksize'],
                        arg['co_varnames']
                        )

    func_res = FunctionType(code_arg, globs)

    func_res.__globals__.update({func_res.__name__: func_res})

    return func_res




