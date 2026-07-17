#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_3.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 17:40:48 by mozay           #+#    #+#               #
#  Updated: 2026/07/17 17:45:14 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_air


def main() -> None:
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py \
using 'from ... import ...' structure")
    print("Testing create_air:", create_air())


if __name__ == "__main__":
    main()
