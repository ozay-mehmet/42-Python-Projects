#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  dark_spellbook.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/18 11:43:05 by mozay           #+#    #+#               #
#  Updated: 2026/07/18 12:03:56 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .dark_validator import validate_dark_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_dark_ingredients(ingredients)

    if "VALID" in result:
        return f"Spell RECORDED {spell_name} ({result})"
    return f"Spell REJECTED {spell_name} ({result})"
