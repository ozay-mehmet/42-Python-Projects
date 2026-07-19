#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  factories.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/19 13:32:17 by mozay           #+#    #+#               #
#  Updated: 2026/07/19 15:34:40 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import abc
from .creature import Creature
from .creatures import Flameling, Aquabub, Pyrodon, Torragon


class CreatureFactory(abc.ABC):
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def create_base(self) -> Creature:
        pass

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def __init__(self):
        super().__init__()

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def __init__(self):
        super().__init__()

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
