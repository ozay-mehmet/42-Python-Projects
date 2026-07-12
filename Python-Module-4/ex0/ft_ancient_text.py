#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/10 19:24:23 by mozay           #+#    #+#               #
#  Updated: 2026/07/12 13:21:10 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import typing


def read_file(filename: str) -> None:
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")
        print("---\n")
        print(file.read(), end="\n\n")
        print("---")
        file.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


def main() -> None:
    if (len(sys.argv) != 2):
        print(f"Usage {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery ===")
    read_file(sys.argv[1])


if __name__ == "__main__":
    main()
