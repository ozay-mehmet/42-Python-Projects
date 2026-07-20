#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  tournament.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/19 18:15:32 by mozay           #+#    #+#               #
#  Updated: 2026/07/20 13:01:14 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex2 import BattleStrategy, StrategyError


def tournament(opponents: list[tuple[CreatureFactory,
                                     BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        factory1, strategy1 = opponents[i]
        for j in range(i + 1, len(opponents)):
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("\n* Battle *")
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except StrategyError as s:
                print("Battle error, aborting tournament:", s)
                return


def main() -> None:
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    flame = FlameFactory()
    normal = NormalStrategy()
    heal = HealingCreatureFactory()
    defensive = DefensiveStrategy()
    tournament([(flame, normal), (heal, defensive)])
    print("\nTournament 2 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    aggressive = AggressiveStrategy()
    tournament([(flame, aggressive), (heal, defensive)])
    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    transform = TransformCreatureFactory()
    aqua = AquaFactory()
    tournament([(aqua, normal), (heal, defensive), (transform, aggressive)])


if __name__ == "__main__":
    main()
