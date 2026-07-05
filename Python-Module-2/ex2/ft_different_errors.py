#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/05 11:44:02 by mozay           #+#    #+#               #
#  Updated: 2026/07/05 14:00:07 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def garden_operations(operation_number) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        45 / 0
    elif operation_number == 2:
        open('/non/existent/file')
    elif operation_number == 3:
        "42" + 42
    elif operation_number == 4:
        print("Operation completed successfully")


def test_error_types() -> None:
    i = 0
    while i < 5:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as v:
            print(f"Caught ValueError: {v}")

        except ZeroDivisionError as z:
            print(f"Caught ZeroDivisionError: {z}")

        except FileNotFoundError as f:
            print(f"Caught FileNotFoundError: {f}")

        except TypeError as t:
            print(f"Caught TypeError: {t}")
        i += 1


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
