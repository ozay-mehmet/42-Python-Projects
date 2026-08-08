#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  functools_artifacts.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/06 16:51:58 by mozay           #+#    #+#               #
#  Updated: 2026/08/08 19:37:01 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any
from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if spells is None:
        return 0
    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(max, spells)
    elif operation == "min":
        return reduce(min, spells)
    else:
        raise ValueError("Unknown operation:", operation)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} enchanted with {element} (Power: {power})"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, power=50, element="Fire"),
        "ice": partial(base_enchantment, power=50, element="Ice"),
        "lightning": partial(base_enchantment, power=50, element="Lightning")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def base(_: Any) -> str:
        return "Unknown spell type"

    @base.register
    def damage(dmg: int) -> str:
        return f"Damage spell: {dmg} damage"

    @base.register
    def enchantment(ench: str) -> str:
        return f"Enchantment: {ench}"

    @base.register(list)
    def multi_cast(spells: list) -> str:
        return f"Multi-cast: {len(spells)} spells"
    return base


def main() -> None:
    print("\nTesting spell reducer...")
    operations = ['add', 'multiply', 'max', 'min']
    spell_powers = [24, 50, 33, 48, 30, 23]
    print("Sum:", spell_reducer(spell_powers, operations[0]))
    print("Product:", spell_reducer(spell_powers, operations[1]))
    print("Max:", spell_reducer(spell_powers, operations[2]))
    print("Min:", spell_reducer(spell_powers, operations[3]))

    print("\nTesting memoized fibonacci...")
    fibonacci_tests = [15, 18, 20]
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    for test in fibonacci_tests:
        print(f"Fib({test}): {memoized_fibonacci(test)}")

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(42))
    print(spell("fireball"))
    print(spell([45, 16, 41]))
    print(spell({"Paris": 42}))

    print("\nTesting partial enchanter...")
    new_partial = partial_enchanter(base_enchantment)
    print(new_partial["fire"](target="Sword"))
    print(new_partial["ice"](target="Shield"))
    print(new_partial["lightning"](target="Bow"))


if __name__ == "__main__":
    main()
