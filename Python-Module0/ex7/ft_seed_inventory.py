#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mozay <mozay@student.42kocaeli.com.tr>       +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 01:07:44 by mozay               #+#    #+#            #
#   Updated: 2026/02/25 01:28:38 by mozay              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        print(f"{seed_type} seeds: {quantity} packets available")
    elif (unit == "grams"):
        print(f"{seed_type} seeds: {quantity} grams total")
    elif (unit == "area"):
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
