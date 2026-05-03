#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mozay <mozay@student.42kocaeli.com.tr>       +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 18:48:20 by mozay               #+#    #+#            #
#   Updated: 2026/02/25 18:53:35 by mozay              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    name: str
    height: float
    age_plant: int

    def __init__(self, name: str, height: float, age_plant: int):
        self.name = name
        self.height = height
        self.age_plant = age_plant

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, \
{self.age_plant} days old")

    def grow(self):
        self.height += 0.8

    def age(self):
        self.age_plant += 1


def main():
    plant = Plant("Rose", 25.0, 30)
    first_height = plant.height
    print("=== Garden Plant Growth ===")
    plant.show()
    i = 1
    while i <= 7:
        print(f"=== Day {i} ===")
        plant.age()
        plant.grow()
        plant.show()
        i += 1
    print(f"Growth this week: {round((plant.height - first_height), 1)}cm")


if __name__ == "__main__":
    main()
