from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
    radio = 'radio'
    visual = 'visual'
    physical = 'physical'
    telepathic = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_contact_rules(self):
        if not self.contact_id.startswith('AC'):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires "
                "at least 3 witnesses"
            )
        if (self.signal_strength > 7.0
                and not self.message_received):
            raise ValueError(
                "Strong signals (>7.0) should include "
                "received messages"
            )
        return (self)


def test():
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        ac1 = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-09-25 22:00",
            location="Area 51, Nevada",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )

        print("Valid contact report:")
        print(f"ID: {ac1.contact_id}")
        print(f"Type: {ac1.contact_type.value}")
        print(f"Location: {ac1.location}")
        print(f"Signal: {ac1.signal_strength}/10")
        print(f"Duration: {ac1.duration_minutes} minutes")
        print(f"Witnesses: {ac1.witness_count}")
        print(f"Message: '{ac1.message_received}'\n")
        print("======================================")
    except ValidationError as e:
        print(e)
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp="2026-09-25 22:30",
            location="Roswell",
            contact_type="telepathic",
            signal_strength=4.5,
            duration_minutes=15,
            witness_count=2,
            is_verified=True
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    test()
