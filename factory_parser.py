import json
import xml.etree.ElementTree as ET
import csv
from io import StringIO

class Parser:
    def parse(self, data):
        pass

class JSONParser(Parser):
    def parse(self, data):
        return json.loads(data)

class XMLParser(Parser):
    def parse(self, data):
        return ET.fromstring(data)

class CSVParser(Parser):
    def parse(self, data):
        reader = csv.reader(StringIO(data))
        return list(reader)

class ParserFactory:
    @staticmethod
    def get_parser(parser_type):
        if parser_type == "json":
            return JSONParser()
        elif parser_type == "xml":
            return XMLParser()
        elif parser_type == "csv":
            return CSVParser()
        else:
            raise ValueError(
                f"지원되지 않는 파서 타입입니다: "
                f"{parser_type}")

# 사용 예시
if __name__ == "__main__":
    data_format = "json"
    data = '{"name": "Alice", "age": 30}'
    parser = ParserFactory.get_parser(data_format)
    parsed_data = parser.parse(data)
    print(parsed_data)
    # 출력: {'name': 'Alice', 'age': 30}

