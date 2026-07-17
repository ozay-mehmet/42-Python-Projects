#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 17:55:51 by mozay           #+#    #+#               #
#  Updated: 2026/07/17 19:14:23 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .elements import create_earth, create_air
from elements import create_water, create_fire


def healing_potion() -> None:
    return f"Healing potion brewed with '{create_earth()}'\
 and '{create_air()}'"


def strength_potion() -> None:
    return f"Strength potion brewed with '{create_fire()}'\
and '{create_water()}'"
