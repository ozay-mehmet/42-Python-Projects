#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_5.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 17:49:52 by mozay           #+#    #+#               #
#  Updated: 2026/07/17 17:51:07 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy import elements


def main() -> None:
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print("Testing create_air:", elements.create_air())


if __name__ == "__main__":
    main()
