class CSVData:
    def get_data(self):
        return "Data from CSV"


class JSONData:
    def get_data(self):
        return "Data from JSON"


def data_processor(data_source):
    print(data_source.get_data())


csv_data = CSVData()
json_data = JSONData()

data_processor(csv_data)   # Output: Data from CSV
data_processor(json_data)  # Output: Data from JSON

