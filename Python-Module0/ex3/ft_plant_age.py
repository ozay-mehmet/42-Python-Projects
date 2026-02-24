#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mozay <mozay@student.42kocaeli.com.tr>       +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 00:07:19 by mozay               #+#    #+#            #
#   Updated: 2026/02/25 01:27:25 by mozay              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plant_age():
    age = int(input("Enter plant age in days: "))

    if (age >= 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
