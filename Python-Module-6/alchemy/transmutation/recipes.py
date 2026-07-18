#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  recipes.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 19:30:50 by mozay           #+#    #+#               #
#  Updated: 2026/07/18 13:26:46 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import elements
from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    return f"Recipe transmuting Lead to Gold: brew '{create_air()}'\
 and '{strength_potion()}' mixed with '{elements.create_fire()}'"
