#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_pipeline.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/15 13:10:25 by mozay           #+#    #+#               #
#  Updated: 2026/07/15 18:37:01 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available")

        return self._rank, self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int] |
               list[float] | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            self._storage.extend(str(x) for x in data)
            self._rank += len(data)
        else:
            self._storage.append(str(data))
            self._rank += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
                return True
        return False

    def ingest(self, data: list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            self._storage.extend(data)
            self._rank += len(data)
        else:
            self._storage.append(data)
            self._rank += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str):
                    return False
                if not isinstance(value, str):
                    return False
            return True
        if isinstance(data, list):
            for dictionary in data:
                if not isinstance(dictionary, dict):
                    return False
                for key, value in dictionary.items():
                    if not isinstance(key, str):
                        return False
                    if not isinstance(value, str):
                        return False
            return True
        return False

    def ingest(self, data: dict[str, str]
               | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            logs = data
        else:
            logs = [data]
        for log in logs:
            self._storage.append(f"{log['log_level']}: {log['log_message']}")
        self._rank += len(logs)


class ExportPlugin(typing.Protocol):
    def __init__(self) -> None:
        super().__init__()

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExport:
    def __init__(self) -> None:
        pass

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        if not data:
            return
        item = ",".join([val for _, val in data])
        print(item)


class JSONExport:
    def __init__(self) -> None:
        pass

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        if not data:
            return
        result: list[str] = []
        offset = min(3, len(data))
        for index, (_, value) in enumerate(data):
            result.append('"item_{}": "{}"'.format(index + offset, value))
        print("{" + ", ".join(result) + "}")


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for value in stream:
            processed = False
            for proc in self.processors:
                try:
                    proc.ingest(value)
                    processed = True
                except ValueError:
                    pass
            if not processed:
                print("DataStream error - Cant process element"
                      " in stream", value)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        else:
            for proc in self.processors:
                cls: type = type(proc)
                print(
                    f"{cls.__name__.replace('Processor', ' Processor')}: "
                    f"total {proc._rank} items processed, "
                    f"remaining {len(proc._storage)} on processor"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            data_output: list[tuple[int, str]] = []
            try:
                for _ in range(nb):
                    value = proc.output()
                    data_output.append(value)
            except Exception:
                pass
            if data_output:
                plugin.process_output(data_output)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print("\nRegistering Processors\n")
    numeric = NumericProcessor()
    data_stream.register_processor(numeric)
    batch_of_data: list[typing.Any] = ['Hello world', [3.14, -1, 2.71], [
        {'log_level': 'WARNING',
         'log_message': 'Telnet access! Use ssh instead'},
        {'log_level': 'INFO',
         'log_message': 'User wil is connected'}],
        42, ['Hi', 'five']]
    print("Send first batch of data on stream:", (batch_of_data))
    print()
    text = TextProcessor()
    log = LogProcessor()
    data_stream.register_processor(text)
    data_stream.register_processor(log)
    data_stream.process_stream(batch_of_data)
    data_stream.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv = CSVExport()
    data_stream.output_pipeline(3, csv)
    print()
    data_stream.print_processors_stats()
    new_batch_of_data: list[typing.Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE', 'log_message':
             'Certificate expires in 10 days'},
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello',
    ]
    print("\nSend another batch of data:", new_batch_of_data)
    data_stream.process_stream(new_batch_of_data)
    print()
    data_stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json = JSONExport()
    data_stream.output_pipeline(5, json)
    print()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
