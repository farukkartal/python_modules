from ex0 import AquaFactory, FlameFactory, CreatureFactory

def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(f"{base.describe()}")
    print(f"{base.attack()}")
    evolved = factory.create_evolved()
    print(f"{evolved.describe()}")
    print(f"{evolved.attack()}")

def start_fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    fighter1 = factory1.create_base()
    fighter2 = factory2.create_base()
    print(f"{fighter1.describe()}")
    print(" vs.")
    print(f"{fighter2.describe()}")
    print(" fight!")
    print(f"{fighter1.attack()}")
    print(f"{fighter2.attack()}")


if __name__ == "__main__":
    aqua = AquaFactory()
    flame = FlameFactory()
    test_factory(flame)
    print("\n")
    test_factory(aqua)
    print("\n")
    print("Testing battle")
    start_fight(flame, aqua)