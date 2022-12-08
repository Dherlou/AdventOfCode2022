from __future__ import annotations
from enum import Enum

from symbols import ActionSymbol, ReactionSymbol, OutcomeSymbol

class Action(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def parse_action(self, action_string: str) -> Action:
        match action_string:
            case ActionSymbol.ROCK.value:
                return Action.ROCK
            case ActionSymbol.PAPER.value:
                return Action.PAPER
            case ActionSymbol.SCISSORS.value:
                return Action.SCISSORS
            case _:
                raise ValueError('Unknown action.')

    @classmethod
    def parse_reaction(self, reaction_string: str) -> Action:
        match reaction_string:
            case ReactionSymbol.ROCK.value:
                return Action.ROCK
            case ReactionSymbol.PAPER.value:
                return Action.PAPER
            case ReactionSymbol.SCISSORS.value:
                return Action.SCISSORS
            case _:
                raise ValueError('Unknown reaction.')

    @classmethod
    def parse_outcome(self, outcome_string: str, action: Action) -> Action:
        match outcome_string:
            case OutcomeSymbol.LOST.value:
                match action:
                    case Action.ROCK:
                        return Action.SCISSORS
                    case Action.PAPER:
                        return Action.ROCK
                    case Action.SCISSORS:
                        return Action.PAPER
            case OutcomeSymbol.DRAW.value:
                return action
            case OutcomeSymbol.WON.value:
                match action:
                    case Action.ROCK:
                        return Action.PAPER
                    case Action.PAPER:
                        return Action.SCISSORS
                    case Action.SCISSORS:
                        return Action.ROCK
            case _:
                raise ValueError('Unknown outcome.')
