#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  creature.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/19 13:29:45 by mozay           #+#    #+#               #
#  Updated: 2026/07/19 16:49:12 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import abc


class Creature(abc.ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abc.abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"
