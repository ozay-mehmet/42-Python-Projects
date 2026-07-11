#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/11 17:28:26 by mozay           #+#    #+#               #
#  Updated: 2026/07/11 17:44:27 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import typing


def read_file(filename: str) -> None:
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO = open(filename, "r")
        print("---\n")
        content = file.read()
        print(content, end="")
        print("\n\n---")
        file.close()
        print(f"File '{filename}' closed.\n")
        print("Transform data:")
        print("---\n")

        new_content = ""
        for char in content:
            if char == "\n":
                new_content += "#\n"
            else:
                new_content += char

        if len(content) > 0 and content[len(content) - 1] != "\n":
            new_content += "#"

        print(new_content, end="")
        print("\n\n---")

        new_filename = input("Enter a new file name (or empty): ")

        if new_filename == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_filename}'")
            new_file: typing.IO = open(new_filename, "w")
            new_file.write(new_content)
            new_file.close()
            print(f"Data saved in file '{new_filename}'.")
    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")
    except FileNotFoundError as file_not_found:
        print(f"Error opening file '{filename}': {file_not_found}")


def main() -> None:
    if (len(sys.argv) != 2):
        print(f"Usage {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    read_file(sys.argv[1])


if __name__ == "__main__":
    main()
