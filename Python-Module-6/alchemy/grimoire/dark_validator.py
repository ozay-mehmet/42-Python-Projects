#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  dark_validator.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/18 11:42:48 by mozay           #+#    #+#               #
#  Updated: 2026/07/18 11:59:44 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()

    for ingredient in allowed:
        if ingredient.lower() in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
