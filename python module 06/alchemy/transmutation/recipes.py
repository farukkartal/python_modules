from elements import create_fire
from alchemy.potions import strength_potion
from ..potions import create_air

def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' and '{strength_potion()}' mixed with '{create_fire()}'")