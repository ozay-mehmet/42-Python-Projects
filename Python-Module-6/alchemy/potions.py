#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 17:55:51 by mozay           #+#    #+#               #
#  Updated: 2026/07/18 13:18:38 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    return f"Healing potion brewed with '{create_earth()}'\
 and '{create_air()}'"


def strength_potion() -> str:
    return f"Strength potion brewed with '{create_fire()}'\
and '{create_water()}'"
