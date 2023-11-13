import csv
import json

class JSONToCSVConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            self.__lines = json.load(json_file)
            print(self.__lines)

    def write_file(self, filename: str):
        if not self.__lines:
            print("No data to write to CSV")
            return

        with open(filename, 'w', newline='') as csv_file:
            if isinstance(self.__lines, list) and all(isinstance(line, dict) for line in self.__lines):
                fieldnames = self.__lines[0].keys()
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for line in self.__lines:
                    writer.writerow(line)
            else:
                print("JSON data is not in the expected format")
            self.cleanup()

    def cleanup(self):
        self.__lines = []

# Тестування адаптера
converter = JSONToCSVConverter()
converter.read_file('example.json')
converter.write_file('converted_example.csv')