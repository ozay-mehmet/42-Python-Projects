#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  space_crew.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/26 14:13:01 by mozay           #+#    #+#               #
#  Updated: 2026/07/26 16:02:57 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)

    def show(self) -> str:
        return f"- {self.name} ({self.rank.value}) - {self.specialization}"


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_validator(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        ranks = [members.rank for members in self.crew]
        if (not (Rank.commander in ranks)) and (not (Rank.captain in ranks)):
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            experienced = [
                members for members in self.crew
                if members.years_experience >= 5
            ]
            if (len(experienced) < len(self.crew) / 2):
                raise ValueError(" Long missions (> 365 days) need 50% "
                                 "experienced crew (5+ years)")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


def true_state() -> None:
    try:
        space = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            launch_date=datetime.now(),
            crew=[
                CrewMember(
                    member_id="SM1",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=30,
                    years_experience=30,
                    specialization="Mission Command"
                ),
                CrewMember(
                    member_id="SM2",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=47,
                    years_experience=30,
                    specialization="Navigation"
                ),
                CrewMember(
                    member_id="SM3",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=52,
                    years_experience=30,
                    specialization="Engineering"
                )
            ],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {space.mission_name}\nID: {space.mission_id}\n\
Destination: {space.destination}\nDuration: {space.duration_days} days\n\
Budget: ${space.budget_millions}M\nCrew size: {len(space.crew)}\n\
Crew members:")
        for members in space.crew:
            print(members.show(), end="\n")
    except ValidationError as e:
        print("Expected validation error:")
        for msg in e.errors():
            print("Mission", msg['msg'][13:])


def false_state() -> None:
    try:
        space = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            launch_date=datetime.now(),
            crew=[
                CrewMember(
                    member_id="SM1",
                    name="Sarah Connor",
                    rank=Rank.cadet,
                    age=30,
                    years_experience=30,
                    specialization="Mission Command"
                ),
                CrewMember(
                    member_id="SM2",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=47,
                    years_experience=30,
                    specialization="Navigation"
                ),
                CrewMember(
                    member_id="SM3",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=52,
                    years_experience=30,
                    specialization="Engineering"
                )
            ],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {space.mission_name}\nID: {space.mission_id}\n\
Destination: {space.destination}\nDuration: {space.duration_days} days\n\
Budget: ${space.budget_millions}M\nCrew size: {len(space.crew)}\n\
Crew members:")
        for members in space.crew:
            print(members.show(), end="\n")
    except ValidationError as e:
        print("Expected validation error:")
        for msg in e.errors():
            print("Mission", msg['msg'][13:])


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    true_state()
    print("\n=========================================")
    false_state()


if __name__ == "__main__":
    main()
