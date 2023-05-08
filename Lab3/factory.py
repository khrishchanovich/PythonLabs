from constants import JSON, XML
from Lab3.Parser.json.json_parser import Json

class Factory(object):

    @staticmethod
    def parser(type: str):
        if type.__eq__(JSON):
            return Json
        elif type.__eq__(XML):
            pass
