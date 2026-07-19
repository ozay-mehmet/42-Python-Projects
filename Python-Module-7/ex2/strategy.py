#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  strategy.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/19 18:17:09 by mozay           #+#    #+#               #
#  Updated: 2026/07/19 18:31:33 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import abc
from ex0 import creature


class BattleStrategy(abc.ABC):
    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def act(self, creature: creature.Creature) -> None:
        pass

    @abc.abstractmethod
    def is_valid(self, creature: creature.Creature) -> bool:
        pass
