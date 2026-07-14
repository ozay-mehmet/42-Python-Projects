#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_stream.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/14 19:17:39 by mozay           #+#    #+#               #
#  Updated: 2026/07/14 20:01:11 by mozay           ###   ########.fr        #
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

        value = self._storage.pop(0)
        rank = self._rank
        self._rank += 1
        return rank, value


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
            for value in data:
                self._storage.append(str(value))
        else:
            self._storage.append(str(data))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return False
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return True
                return False
        return True

    def ingest(self, data: list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            self._storage.extend(data)
        else:
            self._storage.extend(data)


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


class DataStream:
    def __init__(self) -> None:
        self.processor: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processor.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        pass

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processor:
            print("No processor found, no data")
            return


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    numeric = NumericProcessor()
    data_stream.register_processor(numeric)
    batch_of_data: list[typing.Any] = ['Hello world', [3.14, -1, 2.71], [
        {'log_level': 'WARNING',
         'log_message': 'Telnet access! Use ssh instead'},
        {'log_level': 'INFO',
         'log_message': 'User wil is connected'}],
        42, ['Hi', 'five']]
    print("Send first batch of data on stream:", (batch_of_data))
    data_stream.process_stream(batch_of_data)


if __name__ == "__main__":
    main()
