from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy, TacticError

def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("\n* Battle *")
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except TacticError as error:
                print(f"Battle error, aborting tournament: {error}")
                return

if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()
    print("Tournament 0 (basic)")
    battle([(flame, normal), (heal, defensive)])
    print("\nTournament 1 (error)")
    battle([(flame, aggressive), (heal, defensive)])
    print("\nTournament 2 (multiple)")
    battle([(aqua, normal), (heal, defensive), (transform, aggressive)])