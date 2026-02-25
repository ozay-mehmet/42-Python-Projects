#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_summary.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mozay <mozay@student.42kocaeli.com.tr>       +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 01:02:34 by mozay               #+#    #+#            #
#   Updated: 2026/02/25 01:28:20 by mozay              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_garden_summary():
    garden_name = input("Enter garden name: ")
    number_of_plants = input("Enter number of plants: ")
    print(f"Garden: {garden_name}")
    print(f"Plants: {number_of_plants}")
    print("Status: Growing well!")
