#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mozay <mozay@student.42kocaeli.com.tr>       +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 00:20:39 by mozay               #+#    #+#            #
#   Updated: 2026/02/25 01:27:28 by mozay              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative():
    day = int(input("Days until harvest: "))
    count = 1
    while (count <= day):
        print(f"Day {count}")
        count += 1
    print("Harvest time!")
