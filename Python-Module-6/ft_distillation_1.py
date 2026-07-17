#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_distillation_1.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 18:20:59 by mozay           #+#    #+#               #
#  Updated: 2026/07/17 19:30:10 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print("Testing strength_potion:", alchemy.strength_potion())
    print("Testing heal alias:", alchemy.heal())


if __name__ == "__main__":
    main()
