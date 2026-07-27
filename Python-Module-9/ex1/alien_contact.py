#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  alien_contact.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/26 11:50:04 by mozay           #+#    #+#               #
#  Updated: 2026/07/27 12:53:46 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Optional
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_validator(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) "
                             "should include received messages")
        return self


def true_state() -> None:
    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="'Greetings from Zeta Reticuli'"
        )
        print("Valid contact report:")
        print(f"ID: {alien.contact_id}\nType: {alien.contact_type.value}\n\
Location: {alien.location}\nSignal: {alien.signal_strength}/10\n\
Duration: {alien.duration_minutes} minutes\nWitnesses: {alien.witness_count}\n\
Message: {alien.message_received}")
    except ValidationError as e:
        print("Expected validation error:")
        for msg in e.errors():
            print(msg['msg'][13:])


def false_state() -> None:
    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="'Greetings from Zeta Reticuli'"
        )
        print("Valid contact report:")
        print(f"ID: {alien.contact_id}\nType: {alien.contact_type.value}\n\
Location: {alien.location}\nSignal: {alien.signal_strength}/10\n\
Duration: {alien.duration_minutes} minutes\nWitnesses: {alien.witness_count}\n\
Message: {alien.message_received}")
    except ValidationError as e:
        print("Expected validation error:")
        for msg in e.errors():
            print(msg['msg'][13:])


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    true_state()
    print("========================================")
    false_state()


if __name__ == "__main__":
    main()
