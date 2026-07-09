#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/07 16:16:54 by mozay           #+#    #+#               #
#  Updated: 2026/07/09 17:11:45 by mozay           ###   ########.fr        #
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
    achievement_count: int = random.randint(1, len(all_achievements))
    return set(random.sample(all_achievements, achievement_count))


def get_all_achievements(achievements: list[tuple[str, set[str]]]) -> set[str]:
    all_achievements: set[str] = set()
    for _, achieve in achievements:
        all_achievements = all_achievements.union(achieve)
    return all_achievements


def get_common_achievements(
        achievements: list[tuple[str, set[str]]]) -> set[str]:
    common_achievements: set[str] = set()

    first_player: bool = True

    for _, achieve in achievements:
        if first_player:
            common_achievements = achieve
            first_player = False
        else:
            common_achievements = common_achievements.intersection(achieve)
    return common_achievements


def get_unique_achievements(achievements: list[tuple[str, set[str]]],
                            achieve: set[str]) -> set[str]:
    other_players: set[str] = set()

    for _, ach in achievements:
        if ach is not achieve:
            other_players = other_players.union(ach)

    return achieve.difference(other_players)


def get_missing_achievements(all_achievements: set[str],
                             achievement: set[str]) -> set[str]:
    return all_achievements.difference(achievement)


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    players: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    achievements: list[tuple[str, set[str]]] = []

    for player in players:
        gen = gen_player_achievements()
        achievements.append((player, gen))
        print(f"Player {player}: {gen}")

    all_achievements: set[str] = get_all_achievements(achievements)
    print(f"\nAll distinct achievements: {all_achievements}")

    common_achievements: set[str] = get_common_achievements(achievements)
    print(f"\nCommon achievements: {common_achievements}\n")

    for player, achieve in achievements:
        unique = get_unique_achievements(achievements, achieve)
        print(f"Only {player} has: {unique}")

    print()

    game_achievements: set[str] = set(gen_player_achievements())

    for player, achieve in achievements:
        missing: set[str] = get_missing_achievements(
            game_achievements, achieve)
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
