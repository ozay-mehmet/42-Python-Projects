#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  decorator_mastery.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/07 18:42:25 by mozay           #+#    #+#               #
#  Updated: 2026/08/07 19:02:41 by mozay           ###   ########.fr        #
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
    return func


def power_validator(min_power: int) -> Callable:
    return spell_timer


def retry_spell(max_attempts: int) -> Callable:
    return spell_timer


class MageGuild:
    def __init__(self):
        pass

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return True

    def cast_spell(self, spell_name: str, power: int) -> str:
        return spell_name


def main() -> None:
    pass


if __name__ == "__main__":
    main()
