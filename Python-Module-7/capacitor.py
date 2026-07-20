#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  capacitor.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/19 16:21:40 by mozay           #+#    #+#               #
#  Updated: 2026/07/20 12:45:21 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def tranform_capability(capability: TransformCreatureFactory) -> None:
    base = capability.create_base()
    evolved = capability.create_evolved()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def heal_capability(capability: HealingCreatureFactory) -> None:
    base = capability.create_base()
    evolved = capability.create_evolved()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def main() -> None:
    print("Testing Creature with healing capability")
    heal = HealingCreatureFactory()
    heal_capability(heal)
    print("\nTesting Creature with transform capability")
    transform = TransformCreatureFactory()
    tranform_capability(transform)


if __name__ == "__main__":
    main()
