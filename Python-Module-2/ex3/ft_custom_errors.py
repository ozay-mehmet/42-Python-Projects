#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/05 14:01:54 by mozay           #+#    #+#               #
#  Updated: 2026/07/05 17:50:40 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, err: str = "Unknown garden error") -> None:
        super().__init__(err)


class PlantError(GardenError):
    def __init__(self, err: str = "Unknown plant error") -> None:
        super().__init__(err)


class WaterError(GardenError):
    def __init__(self, err: str = "Unknown water error") -> None:
        super().__init__(err)


def test_error_types() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as p:
        print(f"Caught PlantError: {p}")
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as w:
        print(f"Caught WaterError: {w}")
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as g:
        print(f"Caught GardenError: {g}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as g:
        print(f"Caught GardenError: {g}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    test_error_types()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
