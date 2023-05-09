from Lab3.Factory.constants import JSON, XML
from Lab3.Parser.json.json_parser import Json
from Lab3.Parser.xml.xml_parser import Xml


class Factory(object):

    @staticmethod
    def parser(type_: str):
        if type_.__eq__(JSON):
            return Json
        elif type_.__eq__(XML):
            return Xml
        else:
            return Json
