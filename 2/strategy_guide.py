from __future__ import annotations
from enum import Enum
from typing import Tuple

from action import Action


class StrategyGuide:

    def __init__(self, input_file: str, strategy: Strategy):
        self.__guide = self.read_strategy_file(input_file, strategy)

    @property
    def guide(self):
        return self.__guide

    @classmethod
    def read_strategy_file(self, input_file: str, strategy: Strategy) -> list[Action, Action]:
        with open(input_file, 'r') as file:
            lines = [line.strip() for line in file]
            return map(
                lambda line: self.read_strategy_line(line, strategy),
                lines
            )

    @classmethod
    def read_strategy_line(self, line: str, strategy: Strategy) -> Tuple[Action, Action]:
        match line.split():
            case [action, reaction] if strategy == Strategy.ACTION:
                return (Action.parse_action(action), Action.parse_reaction(reaction))
            case [action, outcome] if strategy == Strategy.OUTCOME:
                action = Action.parse_action(action)
                return (action, Action.parse_outcome(outcome, action))
            case _:
                raise ValueError('Missing strategy, action or reaction!')


class Strategy(Enum):
    ACTION = 1
    OUTCOME = 2
