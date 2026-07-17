#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_1.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 17:36:24 by mozay           #+#    #+#               #
#  Updated: 2026/07/17 17:38:08 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from elements import create_water


def main() -> None:
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print("Testing create_water:", create_water())


if __name__ == "__main__":
    main()
