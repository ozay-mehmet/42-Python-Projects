#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_distillation_0.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 18:18:00 by mozay           #+#    #+#               #
#  Updated: 2026/07/17 18:20:06 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print("Testing strength_potion:", strength_potion())
    print("Testing healing_potion:", healing_potion())


if __name__ == "__main__":
    main()
