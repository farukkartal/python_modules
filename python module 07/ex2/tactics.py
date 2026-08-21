import abc
from ex0.abstract_models import Creature
from ex1.advanced_models import HealCapability, TransformCapability

class TacticError(Exception):
    pass

class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise TacticError(f"Invalid Creature '{creature.name}' for normal strategy")
        print(f"{creature.attack()}")

class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, TransformCapability))

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise TacticError(f"Invalid Creature '{creature.name}' for this aggressive strategy")
        isinstance(creature, TransformCapability)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, HealCapability))

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise TacticError(f"Invalid Creature '{creature.name}' for this defensive strategy")
        isinstance(creature, HealCapability)
        print(creature.attack())
        print(creature.heal())