#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  strategies.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/19 18:19:56 by mozay           #+#    #+#               #
#  Updated: 2026/07/20 11:53:27 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .strategy import BattleStrategy
from ex0.creature import Creature
from ex1.capabiliity import TransformCapability, HealCapability


class StrategyError(Exception):
    pass


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "attack")

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}'\
 for this normal strategy")
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, creature: Creature) -> bool:
        return (hasattr(creature, "transform")
                and hasattr(creature, "revert"))

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}'\
 for this aggressive strategy")
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "heal")

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}'\
 for this defensive strategy")
        if isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal())
