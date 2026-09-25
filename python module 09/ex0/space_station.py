from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def test():
    print("Space Station Data Validation")
    print("========================================") 

    try:
        s1 = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-09-25 12:00"
        )
        print("Valid station created:")
        print(f"ID: {s1.station_id}")
        print(f"Name: {s1.name}")
        print(f"Crew: {s1.crew_size} people") 
        print(f"Power: {s1.power_level}%")
        print(f"Oxygen: {s1.oxygen_level}%") 
        if s1.is_operational:
            print("Status: Operational\n")
        else:
            print("Status: Offline\n")
    except ValidationError as e:
        print(e)
    print("========================================") 
    print("Expected validation error:")
    try:
        s2 = SpaceStation(
            station_id="ISS002", 
            name="Test", 
            crew_size=25, 
            power_level=50.0,
            oxygen_level=50.0, 
            last_maintenance="2026-09-25 12:00"
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])

if __name__ == "__main__":
    test()