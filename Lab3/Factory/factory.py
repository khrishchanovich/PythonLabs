from Lab3.Parser.json.json_parser import Json
from Lab3.Parser.xml.xml_parser import Xml


class Factory(object):

    @staticmethod
    def parser(type_: str):
        if type_.__eq__('json'):
            return Json()
        elif type_.__eq__('xml'):
            return Xml()
        else:
            return Json()
