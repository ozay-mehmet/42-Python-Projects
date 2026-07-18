#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  light_spellbook.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/18 11:25:35 by mozay           #+#    #+#               #
#  Updated: 2026/07/18 11:57:58 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    result = validate_ingredients(ingredients)

    if "VALID" in result:
        return f"Spell RECORDED {spell_name} ({result})"
    return f"Spell REJECTED {spell_name} ({result})"
