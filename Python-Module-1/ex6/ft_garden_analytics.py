#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/02 13:29:16 by mozay           #+#    #+#               #
#  Updated: 2026/05/03 14:21:02 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    class _Stats:
        def __init__(self):
            self._grow = 0
            self._age = 0
            self._show = 0

        def inc_grow(self):
            self._grow += 1

        def inc_age(self):
            self._age += 1

        def inc_show(self):
            self._show += 1

        def display(self):
            print(f"Stats: {self._grow} grow, {self._age} age, \
{self._show} show")

    def __init__(self, name, height, age_plant):
        self._name = name
        self._height = height if height >= 0 else 0.0
        self._age_plant = age_plant if age_plant >= 0 else 0
        self._stats = Plant._Stats()

    @staticmethod
    def isOlder(age):
        if (age > 365):
            return f"Is {age} days more than a year? -> True"
        else:
            return f"Is {age} days more than a year? -> False"

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self):
        self._height += 8.0
        self._stats.inc_grow()

    def age(self):
        self._age_plant += 1
        self._stats.inc_age()

    def show(self):
        print(f"{self._name}: {round(self._height, 1)}cm, \
{self._age_plant} days old")
        self._stats.inc_show()

    def show_stats(self):
        self._stats.display()


class Flower(Plant):
    def __init__(self, name, height, age_plant, color):
        super().__init__(name, height, age_plant)
        self.color = color
        self.bloom_ability = False

    def bloom(self) -> None:
        self.bloom_ability = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloom_ability:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age_plant, trunk_diameter):
        super().__init__(name, height, age_plant)
        self.trunk_diameter = trunk_diameter
        self._shade_count = 0

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self):
        print(f"Tree {self._name} now produces a shade of {self._height}cm \
long and {self.trunk_diameter}cm wide.")
        self._shade_count += 1

    def show_stats(self):
        super().show_stats()
        print(f" {self._shade_count} shade")


class Seed(Flower):
    def __init__(self, name, height, age_plant):
        super().__init__(name, height, age_plant, "yellow")
        self._seeds = 0

    def bloom(self):
        super().bloom()
        self._seeds = 42

    def grow(self):
        self._height += 30.0
        self._stats.inc_grow()

    def age(self):
        self._age_plant += 20
        self._stats.inc_age()

    def show(self):
        super().show()
        print(f" Seeds: {self._seeds}")


def showStatus(plant):
    print(f"[statistics for {plant._name}]")
    plant.show_stats()


def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(Plant.isOlder(30))
    print(Plant.isOlder(400))

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    showStatus(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
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
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.bloom()
    sunflower.age()
    sunflower.show()
    showStatus(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    showStatus(unknown)


if __name__ == "__main__":
    main()
