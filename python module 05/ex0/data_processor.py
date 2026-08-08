import abc
import typing

class DataProcessor(abc.ABC):
    def __init__(self):
        self.data = []
        self.rank = 0
    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass
    @abc.abstractmethod
    def ingest(self, data: typing.Any) ->None:
        pass
    def output(self) -> tuple[int, str]:
        first_data = self.data.pop(0)
        current_rank = self.rank
        self.rank = self.rank + 1
        return (current_rank, first_data)

class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, int):
            return True
        if isinstance(data, float):
            return True
        if isinstance(data, list):
            for i in data:
                if not isinstance(i, (int, float)):
                    return False
            return True
        return False
    
    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data) == False:
            raise Exception("Improper numeric data")
        if isinstance (data,list):
            for i in data:
                self.data.append(str(i))
        else:
            self.data.append(str(data))

class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for i in data:
                if not isinstance(i, str):
                    return False
            return True
            
        return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data) == False:
            raise Exception("Improper text data")
        if isinstance(data, list):
            for i in data:
                self.data.append(i)
        else:
            self.data.append(data)

class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for k, v in data.items():
                if not (isinstance(k, str) and isinstance(v, str)):
                    return False
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                for k, v in item.items():
                    if not (isinstance(k, str) and isinstance(v, str)):
                        return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data) == False:
            raise Exception("Improper log data")
            
        if isinstance(data, list):
            for i in data:
                log_text = f"{i['log_level'].strip()}: {i['log_message'].strip()}"
                self.data.append(log_text)
        else:
            log_text = f"{data['log_level'].strip()}: {data['log_message'].strip()}"
            self.data.append(log_text)

def test_numeric_processor():
    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input'42': {num_proc.validate(42)}")
    print(f"Trying to validate input'Hello': {num_proc.validate('Hello')}")
    print("Test invalid ingestion of string'foo' without prior validation:")
    try:
        num_proc.ingest('foo')
    except Exception as e:
        print(f"Got exception: {e}")
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    num_proc.ingest(data)
    
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")


def test_text_processor():
    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    
    print(f"Trying to validate input'42': {text_proc.validate(42)}")
    
    data = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {data}")
    text_proc.ingest(data)
    
    print("Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value {rank}: {val}")


def test_log_processor():
    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    
    print(f"Trying to validate input'Hello': {log_proc.validate('Hello')}")
    
    data = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, 
            {'log_level': 'ERROR ', 'log_message': 'Unauthorized access!!'}]
    print(f"Processing data: {data}")
    log_proc.ingest(data)
    
    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")

if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    test_numeric_processor()
    test_text_processor()
    test_log_processor()