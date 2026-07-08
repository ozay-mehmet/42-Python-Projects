#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_alchemist.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/08 19:06:09 by mozay           #+#    #+#               #
#  Updated: 2026/07/08 19:35:35 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random


def capitalize_players(players: list[str]) -> tuple[list[str], list[str]]:
    capitalized: list[str] = [player.capitalize() for player in players]
    only_capitalized: list[str] = [
        player for player in players if player[0].isupper()]

    return capitalized, only_capitalized


def generate_score(players: list[str]) -> dict[str, int]:
    return {
        player: random.randint(0, 1000)
        for player in players
    }


def calculate_high_score(
        scores: dict[str, int]) -> tuple[float, dict[str, int]]:
    average = sum(scores.values()) / len(scores)
    high_scores = {
        player: score
        for player, score in scores.items()
        if score > average
    }
    return average, high_scores


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam",]

    print(f"Initial list of players: {players}")

    capitalized, players_only_capitalized = capitalize_players(players)
    print(f"New list with all names capitalized: {capitalized}")
    print(f"New list of capitalized names only: {players_only_capitalized}")

    scores = generate_score(capitalized)

    average, high_scores = calculate_high_score(scores)

    print(f"Score dict: {scores}")
    print(f"Score average is {average:.2f}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
