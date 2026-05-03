#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/01 18:21:53 by mozay           #+#    #+#               #
#  Updated: 2026/05/03 12:45:25 by mozay           ###   ########.fr        #
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
            print("Age update rejected\n")
        else:
            self._age_plant = age_plant

    def show(self):
        print(f"Plant created: {self._name}: {self.get_height()}cm, \
{self.get_age()} days old\n")

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
            print("Age update rejected\n")
        else:
            self._age_plant = changed
            print(f"Age updated: {self._age_plant} days\n")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_plant


def main():
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    rose.show()
    rose.set_height(25.0)
    rose.set_age(30)
    rose.set_height(-45)
    rose.set_age(-45)
    print(f"Current state: {rose._name}: {rose.get_height()}cm, \
{rose.get_age()} days old")


if __name__ == "__main__":
    main()
