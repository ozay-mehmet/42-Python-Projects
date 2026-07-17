#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_0.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 17:32:33 by mozay           #+#    #+#               #
#  Updated: 2026/07/17 17:35:41 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import elements


def main() -> None:
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print("Testing create_fire:", elements.create_fire())


if __name__ == "__main__":
    main()
