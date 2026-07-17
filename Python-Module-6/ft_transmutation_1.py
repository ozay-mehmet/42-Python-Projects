#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_transmutation_1.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 19:40:26 by mozay           #+#    #+#               #
#  Updated: 2026/07/17 19:46:01 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print("Testing lead to gold:", alchemy.transmutation.lead_to_gold())


if __name__ == "__main__":
    main()
