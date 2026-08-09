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

    def ingest(
        self,
        data: typing.Union[int, float, list[typing.Union[int, float]]]
    ) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, list):
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

    def ingest(self, data: typing.Union[str, list[str]]) -> None:
        if not self.validate(data):
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

    def ingest(
        self,
        data: typing.Union[dict[str, str], list[dict[str, str]]]
    ) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, list):
            for i in data:
                log_text = f"{i['log_level'].strip()}:"
                f"{i['log_message'].strip()}"
                self.data.append(log_text)
        else:
            log_text = f"{data['log_level'].strip()}:"
            f"{data['log_message'].strip()}"
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
                print(f"DataStream error - Can't process "
                      f"element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for i in self.processors:
            class_name = type(i).__name__
            processor_name = class_name.replace("Processor", " Processor")
            remaining = len(i.data)
            total = remaining + i.rank
            print(f"{processor_name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


def test_main():
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    streamer = DataStream()
    streamer.print_processors_stats()
    print("\nRegistering Numeric Processor")
    num_proc = NumericProcessor()
    streamer.register_processor(num_proc)
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"\nSend first batch of data on stream: {batch}")
    streamer.process_stream(batch)
    streamer.print_processors_stats()
    print("\nRegistering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    streamer.register_processor(text_proc)
    streamer.register_processor(log_proc)
    print("Send the same batch again")
    streamer.process_stream(batch)
    streamer.print_processors_stats()
    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()
    streamer.print_processors_stats()


if __name__ == "__main__":
    test_main()
