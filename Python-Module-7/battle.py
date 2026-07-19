#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  battle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/19 12:39:58 by mozay           #+#    #+#               #
#  Updated: 2026/07/19 13:32:46 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #s

from ex0 import factories


def test_factory(factory: factories.CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: factories.CreatureFactory,
           factory2: factories.CreatureFactory) -> None:
    create_base1 = factory1.create_base()
    create_base2 = factory2.create_base()
    print(create_base1.describe())
    print(" vs.")
    print(create_base2.describe())
    print(" fight!")
    print(create_base1.attack())
    print(create_base2.attack())


def main() -> None:
    flame = factories.FlameFactory()
    aqua = factories.AquaFactory()
    print("Testing factory")
    test_factory(flame)
    print("\nTesting factory")
    test_factory(aqua)
    print("\nTesting battle")
    battle(flame, aqua)


if __name__ == "__main__":
    main()
