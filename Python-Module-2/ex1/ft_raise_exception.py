#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_raise_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mozay <mozay@student.42kocaeli.com.tr>       +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/06 11:08:47 by mozay               #+#    #+#            #
#   Updated: 2026/05/06 11:36:44 by mozay              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(temp_str: str) -> int:
    value = int(temp_str)
    if (value < 0):
        raise Exception(f"{value}°C is too cold for plants (min 0°C)")
    elif (value > 40):
        raise Exception(f"{value}°C is too hot for plants (max 40°C)")
    return value


def display(temperature: str) -> None:
    print(f"\nInput data is '{temperature}'")
    try:
        temperature = input_temperature(temperature)
        print(f"Temperature is now {temperature}°C")
    except Exception as exception:
        print(f"Caught input_temperature error: {exception}")


def test_temperature() -> None:
    temperature = "25"
    display(temperature)
    temperature = "abc"
    display(temperature)
    temperature = "100"
    display(temperature)
    temperature = "-50"
    display(temperature)


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
