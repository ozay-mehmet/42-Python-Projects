#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/08 15:29:41 by mozay           #+#    #+#               #
#  Updated: 2026/07/08 19:53:41 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = ["run", "eat", "sleep", "grab", 
                          "move", "climb", "swim", "release", "use"]
    while True:
        player = players[random.randint(0, len(players) - 1)]
        action = actions[random.randint(0, len(actions) - 1)]
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        yield events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for count in range(1000):
        player, action = next(stream)
        print(f"Event {count}: Player {player} did action {action}")

    events = []

    for _ in range(10):
        events.append(next(stream))

    print("Built list of 10 events:", events)

    for event in consume_event(events):
        print("Got event from list:", event)
        print("Remains in list:", events)


if __name__ == "__main__":
    main()
