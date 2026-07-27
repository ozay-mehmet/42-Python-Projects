#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  space_station.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/25 19:17:48 by mozay           #+#    #+#               #
#  Updated: 2026/07/27 12:53:24 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def true_state() -> None:
    try:
        space = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="Operational"
        )
        print("Valid station created:")
        status = "Operational" if space.is_operational else "Non-Operational"
        print(f"ID: {space.station_id}\nName: {space.name}\n\
Crew: {space.crew_size} people\nPower: {space.power_level}%\n\
Oxygen: {space.oxygen_level}%\nStatus: {status}\n")
    except ValidationError as e:
        print("Expected validation error:")
        for msg in e.errors():
            print(msg['msg'])


def false_state() -> None:
    try:
        space = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=45,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="Operational"
        )
        print("Valid station created:")
        status = "Operational" if space.is_operational else "Non-Operational"
        print(f"ID: {space.station_id}\nName: {space.name}\n\
Crew: {space.crew_size} people\nPower: {space.power_level}%\n\
Oxygen: {space.oxygen_level}%\nStatus: {status}\n")
    except ValidationError as e:
        print("Expected validation error:")
        for msg in e.errors():
            print(msg['msg'])


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    true_state()
    print("========================================")
    false_state()


if __name__ == "__main__":
    main()
