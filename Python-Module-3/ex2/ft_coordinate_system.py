#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/06 19:13:42 by mozay           #+#    #+#               #
#  Updated: 2026/07/07 16:20:41 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        message = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = message.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            coordinates: tuple[float, float, float] = (
                float(parts[0].strip()),
                float(parts[1].strip()),
                float(parts[2].strip()),
            )
            return coordinates
        except ValueError:
            for part in parts:
                try:
                    float(part.strip())
                except ValueError as v:
                    print(f"Error on parameter '{part.strip()}': {v}")
                    break


def calculate_distance(
        coordinate_1: tuple[float, float, float],
        coordinate_2: tuple[float, float, float]
) -> float:
    x1, y1, z1 = coordinate_1
    x2, y2, z2 = coordinate_2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def main() -> None:
    center: tuple[float, float, float] = (0.0, 0.0, 0.0)
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_set = get_player_pos()
    print(f"Got a first tuple: {first_set}")
    print(f"It includes: X={first_set[0]}, Y={first_set[1]}, Z={first_set[2]}")
    print(f"Distance to center: {calculate_distance(center, first_set):.4f}")
    print("\nGet a second set of coordinates")
    second_set = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: \
{calculate_distance(first_set, second_set):.4f}")


if __name__ == "__main__":
    main()
