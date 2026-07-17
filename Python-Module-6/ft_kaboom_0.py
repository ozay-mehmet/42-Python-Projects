#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_kaboom_0.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 19:53:48 by mozay           #+#    #+#               #
#  Updated: 2026/07/17 19:55:10 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===\nUsing grimoire module directly")
    print("Testing record light spell:", alchemy.grimoire.dark_spellbook())


if __name__ == "__main__":
    main()
