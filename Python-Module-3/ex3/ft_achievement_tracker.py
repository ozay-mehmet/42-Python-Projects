#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/07 16:16:54 by mozay           #+#    #+#               #
#  Updated: 2026/07/08 13:49:52 by mozay           ###   ########.fr        #
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


def get_common_achievements(players: dict[str, set[str]]) -> set[str]:
    common_achievements: set[str] = set()

    first_player: bool = True

    for player in players:
        if first_player:
            common_achievements = players[player]
            first_player = False
        else:
            common_achievements = common_achievements.intersection(
                players[player])
        return common_achievements


def get_unique_achievements(player_name: str,
                            players: dict[str, set[str]]) -> set[str]:
    other_players: set[str] = set()

    for player in players:
        if player != player_name:
            other_players = other_players.union(players[player])

    return players[player_name].difference(other_players)


def get_missing_achievements(player_name: str, all_achievements: set[str],
                             players: dict[str, set[str]]) -> set[str]:
    return all_achievements.difference(players[player_name])


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
        }

    for player in players:
        print(f"Player {player}: {players[player]}")

    all_achievements: set[str] = get_all_achievements(players)
    print(f"\nAll distinct achievements: {all_achievements}")

    common_achievements: set[str] = get_common_achievements(players)
    print(f"\nCommon achievements: {common_achievements}\n")

    for player in players:
        unique = get_unique_achievements(player, players)
        print(f"Only {player} has: {unique}")

    print()

    game_achievements: set[str] = set(gen_player_achievements())

    for player in players:
        missing: set[str] = get_missing_achievements(
            player,
            game_achievements,
            players,
        )
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
