#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/01 18:32:06 by mozay           #+#    #+#               #
#  Updated: 2026/05/03 12:21:41 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    name: str
    height: float
    age_plant: int

    def __init__(self, name: str, height: float, age_plant: int):
        self.name = name
        self.height = height
        self.age_plant = age_plant

    def show(self):
        print(f"Created: {self.name}: {round(self.height, 1)}cm, \
{self.age_plant} days old")


def main():
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    print("=== Plant Factory Output ===")
    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()


if __name__ == "__main__":
    main()
