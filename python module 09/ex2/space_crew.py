from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    cadet = 'cadet'
    officer = 'officer'
    lieutenant = 'lieutenant'
    captain = 'captain'
    commander = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_mission_rules(self):
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")
        has_leader = False
        for member in self.crew:
            if member.rank == Rank.commander or member.rank == Rank.captain:
                has_leader = True
                break
        if not has_leader:
            raise ValueError(
                "Mission must have at least one "
                "Commander or Captain"
            )
        if self.duration_days > 365:
            experienced_count = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_count += 1
            if experienced_count < (len(self.crew) / 2):
                raise ValueError(
                    "Long missions (> 365 days) need "
                    "50% experienced crew"
                )

        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return (self)


def test():
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        c1 = CrewMember(
            member_id="C001", name="Sarah Connor", rank="commander",
            age=45, specialization="Mission Command", years_experience=15
        )
        c2 = CrewMember(
            member_id="C002", name="John Smith", rank="lieutenant",
            age=35, specialization="Navigation", years_experience=8
        )
        c3 = CrewMember(
            member_id="C003", name="Alice Johnson", rank="officer",
            age=28, specialization="Engineering", years_experience=3
        )
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-10-01 08:00",
            duration_days=900,
            crew=[c1, c2, c3],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(
                f"- {member.name} ({member.rank.value}) "
                f"- {member.specialization}"
            )
        print()
    except ValidationError as e:
        print(e)
    print("=========================================")
    print("Expected validation error:")
    try:
        c_fail1 = CrewMember(
            member_id="C004", name="Bob", rank="officer",
            age=30, specialization="Science", years_experience=5
        )
        c_fail2 = CrewMember(
            member_id="C005", name="Charlie", rank="lieutenant",
            age=32, specialization="Medical", years_experience=6
        )

        SpaceMission(
            mission_id="M2025_MOON",
            mission_name="Moon Base Alpha",
            destination="Moon",
            launch_date="2026-11-01 08:00",
            duration_days=30,
            crew=[c_fail1, c_fail2],
            budget_millions=500.0
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    test()
