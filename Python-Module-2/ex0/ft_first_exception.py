#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mozay <mozay@student.42kocaeli.com.tr>       +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/06 09:57:10 by mozay               #+#    #+#            #
#   Updated: 2026/05/06 11:03:36 by mozay              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    temperature = "25"
    print(f"Input data is '{temperature}'")
    try:
        temp_temperature = input_temperature(temperature)
        print(f"Temperature is now {temp_temperature}°C\n")
    except ValueError as exception:
        print(f"Caught input_temperature error: {exception}")
    temperature = "abc"
    print(f"Input data is '{temperature}'")
    try:
        temp_temperature = input_temperature(temperature)
        print(f"Temperature is now {temp_temperature}°C\n")
    except ValueError as exception:
        print(f"Caught input_temperature error: {exception}")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
