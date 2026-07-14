#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_processor.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/14 14:55:20 by mozay           #+#    #+#               #
#  Updated: 2026/07/14 19:15:25 by mozay           ###   ########.fr        #
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


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(" Trying to validate input '42':", numeric.validate(42))
    print(" Trying to validate input 'Hello':", numeric.validate("Hello"))
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as v:
        print(" Got exception:", v)
    print(" Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print(" Extracting 3 values..")
    for _ in range(3):
        rank, value = numeric.output()
        print(f" Numeric value {rank}: {value}")
    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(" Trying to validate input '42':", text.validate(42))
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])
    print(" Extracting 1 value...")
    rank, value = text.output()
    print(f" Text value {rank}: {value}")
    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(" Trying to validate input '42'", log.validate(42))
    print(" Processing data: [{'log_level': 'NOTICE', 'log_message': "
          "'Connection to server'}, {'log_level': 'ERROR', 'log_message': "
          "'Unauthorized access!!'}]")
    log.ingest([{"log_level": "NOTICE", "log_message": "Connection to server"},
                {
                    "log_level": "ERROR",
                    "log_message": "Unauthorized access!!"
                 }])
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f" Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
