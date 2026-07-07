#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/07 16:16:54 by mozay           #+#    #+#               #
#  Updated: 2026/07/07 19:14:20 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random


def gen_player_achievements() -> set[str]:
    all_achievements: list[str] = [
        "First Steps", "Survivor", "Boss Slayer", "Collector Supreme",
        "Treasure Hunter", "Speed Runner", "Untouchable",
        "World Savior", "Master Explorer", "Crafting Genius",
        "Strategist", "Sharp Mind", "Hidden Path Finder",
    ]
    achievement_count: int = random.randint(4, len(all_achievements))
    return set(random.sample(all_achievements, achievement_count))


def get_all_achievements(players: dict[str, set[str]]) -> set[str]:
    all_achievements: set = set()
    for player in players:
        all_achievements = all_achievements.union(players[player])
    return all_achievements


def main() -> None:
    print("=== Achievement Tracker System ===\n")


if __name__ == "__main__":
    main()
