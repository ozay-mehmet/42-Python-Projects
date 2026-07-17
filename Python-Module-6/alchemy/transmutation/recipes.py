#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  recipes.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 19:30:50 by mozay           #+#    #+#               #
#  Updated: 2026/07/17 19:39:54 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy
import alchemy.potions


def lead_to_gold() -> str:
    return f"Recipe transmuting Lead to Gold: brew '{alchemy.create_air()}'\
 and '{alchemy.potions.strength_potion()}'\
 mixed with '{alchemy.potions.create_fire()}'"
