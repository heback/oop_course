# 믹스인 정의
class LoggingMixin:
    def log(self, message):
        print(f"[LOG]: {message}")


class DataProcessor:
    def process_data(self, data):
        print(f"Processing data: {data}")


# DataProcessor에 LoggingMixin 기능을 추가
class ProcessWithLogging(DataProcessor, LoggingMixin):
    def process_data(self, data):
        self.log("Start processing")
        super().process_data(data)
        self.log("Processing finished")


# 사용
processor = ProcessWithLogging()
processor.process_data("Sample Data")

