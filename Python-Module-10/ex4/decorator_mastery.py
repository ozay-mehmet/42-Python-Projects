#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  decorator_mastery.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/07 18:42:25 by mozay           #+#    #+#               #
#  Updated: 2026/08/08 16:31:22 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Callable
from functools import wraps
from time import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def timer() -> str:
        print("Casting", func.__name__ + "...")
        start = time()
        func_wrap = func()
        end = time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return func_wrap
    return timer


def power_validator(min_power: int) -> Callable:
    def decorator_factory(func: Callable) -> Callable:
        @wraps(func)
        def check_power(self, spell_name, power):
            if power < min_power:
                return "Insufficient power for this spell"
            return func(self, spell_name, power)
        return check_power
    return decorator_factory


def retry_spell(max_attempts: int) -> Callable:
    def decarator(func: Callable) -> Callable:
        @wraps(func)
        def check_spell() -> Callable | str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func()
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying...\
(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return check_spell
    return decarator


class MageGuild:
    def __init__(self):
        pass

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name.strip()) >= 3 and all(
            char.isspace() or char.isalpha() for char in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Succesfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


@retry_spell(3)
def unstable_spell() -> str:
    raise Exception("Spell fizzled")


def main() -> None:
    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")
    result = unstable_spell()
    print(result)
    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    mage = MageGuild()

    test_powers = [15, 12, 45, 7]
    spell_names = ['shield', 'lightning', 'freeze', 'fireball']
    mage_names = ['Ash', 'Phoenix', 'Morgan', 'River', 'Storm', 'Casey']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print(MageGuild.validate_mage_name(mage_names[0]))
    print(MageGuild.validate_mage_name(invalid_names[0]))
    print(mage.cast_spell(spell_names[1].capitalize(), test_powers[0]))
    print(mage.cast_spell(spell_names[1].capitalize(), test_powers[3]))


if __name__ == "__main__":
    main()
