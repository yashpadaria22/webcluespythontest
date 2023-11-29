
import json ,csv
class FileParser:
    def __init__(self, path):
        self.file_path = path

    def parse(self):
        pass
    
class CSVparser(FileParser):
   
    def parse(self):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            CSV_data = [row for row in reader]
        return CSV_data
    
class JSONparser(FileParser):
    
    def parse(self):
        with open(self.file_path, 'r') as file:
            JSON_data = json.load(file)
        return JSON_data

class TextFileParser(FileParser):
    def parse(self):
        with open(self.file_path, 'r') as file:
            TEXT_data = file.read()
        return TEXT_data

csv_parser = CSVparser('CSVsample.csv')
csv_data = csv_parser.parse()
print(f"CSV Data:\n {csv_data} \n")

json_parser = JSONparser('JSONsample.json')
json_data = json_parser.parse()
print(f"\nJSON Data:\n {json_data} \n")


text_parser = TextFileParser('TEXTsample.txt')
text_data = text_parser.parse()
print(f"\nText Data:\n {text_data} \n")
 