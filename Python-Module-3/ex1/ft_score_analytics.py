#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/06 17:55:56 by mozay           #+#    #+#               #
#  Updated: 2026/07/06 19:11:28 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def score_analytics() -> None:
    score_list: list[int] = []
    i = 1
    total_arg = len(sys.argv) - 1
    while i <= total_arg:
        try:
            score_list.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1
    if len(score_list) == 0:
        print("No scores provided. Usage: \
python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {score_list}")
        print(f"Total score: {sum(score_list)}")
        print(f"Average score: {sum(score_list) / len(score_list)}")
        print(f"High score: {max(score_list)}")
        print(f"Low score: {min(score_list)}")
        print(f"Score range: {max(score_list) - min(score_list)}")


def main() -> None:
    print("=== Player Score Analytics ===")
    score_analytics()


if __name__ == "__main__":
    main()
