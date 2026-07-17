#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_2.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 17:38:28 by mozay           #+#    #+#               #
#  Updated: 2026/07/17 17:40:14 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.elements


def main() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth:", alchemy.elements.create_earth())


if __name__ == "__main__":
    main()
