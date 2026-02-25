#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mozay <mozay@student.42kocaeli.com.tr>       +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 00:07:30 by mozay               #+#    #+#            #
#   Updated: 2026/02/25 01:27:26 by mozay              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder():
    day = int(input("Days since last watering: "))
    if (day >= 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
