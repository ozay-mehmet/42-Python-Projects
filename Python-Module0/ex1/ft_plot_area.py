#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plot_area.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mozay <mozay@student.42kocaeli.com.tr>       +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 01:27:21 by mozay               #+#    #+#            #
#   Updated: 2026/02/25 01:27:22 by mozay              ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    plotArea = length * width
    print(f"Plot area: {plotArea}")
