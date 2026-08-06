#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  scope_mysteries.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/06 15:03:04 by mozay           #+#    #+#               #
#  Updated: 2026/08/06 16:50:36 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def increment_count() -> int:
        nonlocal count
        count += 1
        return count
    return increment_count


def spell_accumulator(initial_power: int) -> Callable:
    def add_power(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power
    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def display_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return display_enchantment


def memory_vault() -> dict[str, Callable]:
    memory: dict = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> str:
        if key not in memory:
            return "Memory not found"
        else:
            return memory[key]
    return {"store": store, "recall": recall}


def main() -> None:
    print("\nTesting mage counter...")
    counter_a = mage_counter()
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("counter_a call 1", counter_a())
    print("counter_a call 2", counter_a())
    print("counter_b call 1", counter_b())
    print("\nTesting spell accumulator...")
    initial_powers = [65, 38, 63]
    power_additions = [11, 19, 12]
    spell = spell_accumulator(initial_powers[0])
    print("Base", str(initial_powers[0]) + ",", "add",
          str(power_additions[0]) + ":", spell(power_additions[0]))
    print("Base", str(initial_powers[0]) + ",", "add",
          str(power_additions[1]) + ":", spell(power_additions[1]))
    print("\nTesting enchantment factory...")
    enchantment_types = ['Radiant', 'Flaming', 'Earthen']
    items_to_enchant = ['Armor', 'Shield', 'Ring', 'Staff']
    enchanment = enchantment_factory(enchantment_types[1])
    print(enchanment(items_to_enchant[0]))
    enchanment = enchantment_factory(enchantment_types[0])
    print(enchanment(items_to_enchant[1]))
    print("\nTesting memory vault...")
    store, recall = memory_vault().values()
    print("Store 'secret' = 42")
    store("secret", 42)
    print("Recall 'secret':", recall("secret"))
    print("Recall 'unknown':", recall("unknown"))


if __name__ == "__main__":
    main()
