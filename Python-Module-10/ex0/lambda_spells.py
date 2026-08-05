#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/28 18:47:15 by mozay           #+#    #+#               #
#  Updated: 2026/08/05 19:51:40 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def spell_transformer(spells: list[str]) -> list[str]:
    mapped = list(map(lambda spell: f"* {spell} *", spells))
    return mapped


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filter_mages = list(filter(
        lambda power: power['power'] >= min_power, mages))
    return filter_mages


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(artifacts,
                              key=lambda artifacts: artifacts['power'])
    return sorted_artifacts


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda max: max['power'])['power']
    min_power = min(mages, key=lambda min: min['power'])['power']
    average_power = round(sum(map(
        lambda average: average['power'], mages)) / len(mages), 2)
    return {'max_power': max_power,
            'min_power': min_power, 'avg_power': average_power}


def main() -> None:
    print("\nTesting artifact sorter...")
    artifacts = [{'name': 'Fire Staff', 'power': 83, 'type': 'focus'},
                 {'name': 'Lightning Rod', 'power': 93, 'type': 'accessory'},
                 {'name': 'Crystal Orb', 'power': 102, 'type': 'weapon'},
                 {'name': 'Fire Staff', 'power': 70, 'type': 'focus'}]
    sorted_artifacts = artifact_sorter(artifacts)
    max_value_of_artifact = max(sorted_artifacts, key=lambda max: max['power'])
    name_max = max_value_of_artifact['name']
    max_power = max_value_of_artifact['power']
    min_value_of_artifact = min(sorted_artifacts, key=lambda min: min['power'])
    name_min = min_value_of_artifact['name']
    min_power = min_value_of_artifact['power']
    print(f"{name_max} ({max_power} power) comes "
          f"before {name_min} ({min_power} power)")
    print("\nTesting spell transformer...")
    spells = ['shield', 'freeze', 'fireball', 'heal']
    transformed_spells = spell_transformer(spells)
    for spell in transformed_spells:
        print(spell, end=" ")
    print("\n\nTesting mage stats...")
    mages = [{'name': 'Ash', 'power': 94, 'element': 'wind'},
             {'name': 'Rowan', 'power': 77, 'element': 'lightning'},
             {'name': 'Phoenix', 'power': 58, 'element': 'wind'},
             {'name': 'Jordan', 'power': 71, 'element': 'water'},
             {'name': 'Jordan', 'power': 95, 'element': 'wind'}]
    mages_list = mage_stats(mages)
    print(f"Max power is {mages_list['max_power']}")
    print(f"Min power is {mages_list['min_power']}")
    print(f"Average power is {mages_list['avg_power']}")
    print("\n\nTesting power filter")
    power = 90
    power_list = power_filter(mages, power)
    for powers in power_list:
        print(f"Artifacts power is more than {power}: "
              f"{powers['name']} and {powers['name']}'s "
              f"power is {powers['power']}")


if __name__ == "__main__":
    main()
