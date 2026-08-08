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
    def ingest(self, data: typing.Any) -> None:
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


class DataStream:
    def __init__(self):
        self.processors = []
        
    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for data in stream:
            is_processed = False
            for i in self.processors:
                if not is_processed and i.validate(data):
                    i.ingest(data)
                    is_processed = True
            if not is_processed:
                print(f"DataStream error - Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data\n")
            return
            
        for i in self.processors:
            processor_name = type(i).__name__.replace("Processor", " Processor")
            remaining = len(i.data)
            total = remaining + i.rank
            print(f"{processor_name}: total {total} items processed, remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            extracted_data = []
            for _ in range(nb):
                if proc.data: 
                    extracted_data.append(proc.output())
            if extracted_data:
                plugin.process_output(extracted_data)


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...

class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        csv_string = ""
        count = 0
        for item in data:
            value = item[1]
            csv_string = csv_string + value
            count = count + 1
            if count < len(data):
                csv_string = csv_string + ","
        print(csv_string)

class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        json_string = "{"
        count = 0
        
        for item in data:
            rank = str(item[0])
            value = item[1]
            json_string = json_string + f'"item_{rank}": "{value}"'
            count = count + 1
            if count < len(data):
                json_string = json_string + ", "
        json_string = json_string + "}"
        print(json_string)

def test_main():
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    streamer = DataStream()
    streamer.print_processors_stats()
    print("Registering Processors\n")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    streamer.register_processor(num_proc)
    streamer.register_processor(text_proc)
    streamer.register_processor(log_proc)
    batch1 = ['Hello world', [3.14,-1, 2.71], [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {batch1}\n")
    streamer.process_stream(batch1)
    streamer.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    streamer.output_pipeline(3, csv_plugin)
    streamer.print_processors_stats()
    batch2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'], [{'log_level': 'ERROR', 'log_message': '500 server crash'}, {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"\nSend another batch of data: {batch2}")
    streamer.process_stream(batch2)
    streamer.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    streamer.output_pipeline(5, json_plugin)
    streamer.print_processors_stats()

if __name__ == "__main__":
    test_main()