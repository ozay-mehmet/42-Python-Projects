#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  higher_magic.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/06 12:10:40 by mozay           #+#    #+#               #
#  Updated: 2026/08/08 19:36:45 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any
from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> Any:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def casted(target: str, power: int) -> str:
        if condition(target, power) is True:
            return spell(target, power)
        else:
            return "Spell fizzled"
    return casted


def spell_sequence(spells: list[Callable]) -> Callable:
    def spell_result(target: str, power: int) -> list:
        spell_lists: list = []
        for spell in spells:
            spell_lists.append(spell(target, power))
        return spell_lists
    return spell_result


def print_result(target: str, power: int) -> str:
    return f"Creature: '{target}' - Power: '{power}'\nCombined spell result: "


def test_result(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} power, Heals {target}"


def test_power(target: str, power: int) -> str:
    return f"Amplified: {power}\nCreature: {target}"


def display(target: str, power: int) -> str:
    return f"Creature: '{target}' - Power: '{power}'"


def main() -> None:
    print("\nTesting spell combiner...")
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    test_spell = spell_combiner(print_result, test_result)
    text, result = test_spell(test_targets[0], 45)
    print(text, result)
    print("\nTesting power amplifier...")
    test_values = [12, 11, 10, 45]
    test_amplifier = power_amplifier(test_power, 3)
    print(f"Original: {test_values[2]}, "
          f"{test_amplifier(test_targets[3], test_values[2])}")
    print("\nTesting conditional caster...")
    conditioned = conditional_caster(lambda _, x: x >= 45, test_result)
    print(conditioned(test_targets[1], test_values[3]))
    print(conditioned(test_targets[1], test_values[1]))
    print("\nTesting spell sequence...")
    sequence = spell_sequence([test_result, display])
    text, result = sequence(test_targets[2], test_values[0])
    print(f"{text}\n{result}")


if __name__ == "__main__":
    main()
