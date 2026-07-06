#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/06 14:04:40 by mozay           #+#    #+#               #
#  Updated: 2026/07/06 17:54:19 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def common_quest() -> None:
    total_arg = len(sys.argv)
    print(f"Program name: {sys.argv[0]}")
    if total_arg <= 1:
        print("No arguments provided!")
    else:
        i = 1
        print(f"Arguments received: {total_arg - 1}")
        while i < total_arg:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {total_arg}")


def main() -> None:
    print("=== Command Quest ===")
    common_quest()


if __name__ == "__main__":
    main()
