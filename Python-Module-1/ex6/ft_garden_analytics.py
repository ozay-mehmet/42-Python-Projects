#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/02 13:29:16 by mozay           #+#    #+#               #
#  Updated: 2026/05/02 19:48:44 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    _name: str
    _height: int
    _age_plant: int

    def __init__(self, name: str, height: int, age_plant: int) -> None:
        self._name = name
        if (height < 0):
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
        if (age_plant < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_plant = age_plant

    @staticmethod
    def isOlder(age):
        if (age > 365):
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

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

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age_plant

    def age(self):
        self._age_plant += 1

    def grow(self):
        self._height += 2.1

    def show(self):
        print(f"{self._name}: {round(self.get_height(), 1)}cm, \
{self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name, height, age_plant, color):
        super().__init__(name, height, age_plant)
        self.color = color
        self.ability = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")

    def bloom(self) -> None:
        if not (self.ability):
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")
            self.ability = False


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


class Seed(Flower):
    def __init__(
            self,
            name,
            height,
            age_plant
    ):
        super().__init__(name, height, age_plant, "yellow")
        self.seed_quantity = 0

    def show(self) -> None:
        super().show()

    def bloom(self):
        if (self.ability):
            super().bloom()
            print(f" Seeds: {self.seed_quantity}")


def showStatus(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    print(f"Stats: {plant.grow()} grow, {plant.get_age()} age, \
{plant.show()} show")


def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.isOlder(30)
    Plant.isOlder(400)
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    showStatus(rose)
    print("[asking the rose to grow and bloom]")
    rose.show()
    rose.bloom()
    showStatus(rose)
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    showStatus(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    showStatus(oak)
    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45)
    sunflower.show()
    sunflower.bloom()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.show()

if __name__ == "__main__":
    main()
