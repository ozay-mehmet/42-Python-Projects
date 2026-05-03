#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/02 13:29:16 by mozay           #+#    #+#               #
#  Updated: 2026/05/03 14:18:25 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    _name: str
    _height: float
    _age_plant: int

    def __init__(self, name: str, height: float, age_plant: int) -> None:
        self._name = name
        if (height < 0.0):
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
        if (age_plant < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_plant = age_plant

    def set_height(self, changed) -> None:
        if changed < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = changed
            print(f"Height updated: {self._height}cm")

    def set_age(self, changed) -> None:
        if changed < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_plant = changed
            print(f"Age updated: {self._age_plant} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_plant

    def age(self):
        self._age_plant += 1

    def grow(self):
        self._height += 2.1

    def show(self) -> None:
        print(f"{self._name}: {round(self.get_height(), 1)}cm, \
{self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name, height, age_plant, color):
        super().__init__(name, height, age_plant)
        self.color = color
        self.bloom_ability = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")

    def bloom(self) -> None:
        if (self.bloom_ability):
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")
            self.bloom_ability = True


class Tree(Plant):
    def __init__(
            self,
            name,
            height,
            age_plant,
            trunk_diameter
    ):
        super().__init__(name, height, age_plant)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of \
{self._height}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
            self,
            name,
            height,
            age_plant,
            harvest_season,
    ):
        super().__init__(name, height, age_plant)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def age(self):
        super().age()
        self.nutritional_value += 1


def main():
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    print("[asking the rose to bloom]")
    rose.show()
    rose.bloom()
    print("\n=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print("\n=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April")
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    i = 1
    while (i <= 20):
        vegetable.grow()
        vegetable.age()
        i += 1
    vegetable.show()


if __name__ == "__main__":
    main()
