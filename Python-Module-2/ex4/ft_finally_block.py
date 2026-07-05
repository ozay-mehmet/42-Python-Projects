#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/05 14:53:24 by mozay           #+#    #+#               #
#  Updated: 2026/07/05 15:24:25 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class PlantError(Exception):
    def __init__(self, plant_name):
        super().__init__(plant_name)


def water_plant(plant_name) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        plants = ['Tomato', 'Lettuce', 'Carrots']
        for i in plants:
            water_plant(i)
    finally:
        print("Closing watering system")
    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as p:
        print(f"Caught PlantError: {p}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===")
    test_watering_system()


if __name__ == "__main__":
    main()
