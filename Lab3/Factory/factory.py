from Lab3.Factory.constants import JSON, XML
from Lab3.Parser.json.json_parser import Json


class Factory(object):

    @staticmethod
    def parser(type_: str):
        if type_.__eq__(JSON):
            return Json
        else:
            return Json
