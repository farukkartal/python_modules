from ex1 import HealingCreatureFactory, TransformCreatureFactory

def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    print(f"{base.describe()}")
    print(f"{base.attack()}")
    print(f"{base.heal()}")
    print(" evolved:")
    evolved = factory.create_evolved()
    print(f"{evolved.describe()}")
    print(f"{evolved.attack()}")
    print(f"{evolved.heal()}")

def test_transforming(factory: TransformCreatureFactory) -> None:
    print("\nTesting Creature with transform capability")
    print(" base:")
    base = factory.create_base()
    print(f"{base.describe()}")
    print(f"{base.attack()}")
    print(f"{base.transform()}")
    print(f"{base.attack()}")
    print(f"{base.revert()}")
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())

if __name__ == "__main__":
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    test_healing(heal)
    test_transforming(transform)