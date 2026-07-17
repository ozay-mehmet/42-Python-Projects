#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_transmutation_0.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 19:34:56 by mozay           #+#    #+#               #
#  Updated: 2026/07/17 19:36:39 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print("Testing lead to gold:",
          alchemy.transmutation.recipes.lead_to_gold())


if __name__ == "__main__":
    main()
