#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  capabiliity.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/19 16:22:53 by mozay           #+#    #+#               #
#  Updated: 2026/07/19 18:05:11 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import abc


class HealCapability(abc.ABC):
    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(abc.ABC):
    def __init__(self) -> None:
        self.transformed = False
        super().__init__()

    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass
