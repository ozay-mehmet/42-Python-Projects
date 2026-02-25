#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mozay <mozay@student.42kocaeli.com.tr>       +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 00:18:22 by mozay               #+#    #+#            #
#   Updated: 2026/02/25 01:27:31 by mozay              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))

    def count_day(current_day, end_day):
        if current_day > end_day:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        count_day(current_day + 1, end_day)

    count_day(1, day)
