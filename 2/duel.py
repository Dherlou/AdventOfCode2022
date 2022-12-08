from __future__ import annotations

from action import Action
from result import Result


class Duel:

    @classmethod
    def play(self, action: Action, reaction: Action) -> int:
        return self.__outcome(action, reaction).value.score + reaction.value

    @classmethod
    def __outcome(self, action: Action, reaction: Action) -> Result:
        match action:
            case Action.ROCK:
                match reaction:
                    case Action.ROCK:
                        return Result.DRAW
                    case Action.PAPER:
                        return Result.WON
                    case Action.SCISSORS:
                        return Result.LOST
            case Action.PAPER:
                match reaction:
                    case Action.ROCK:
                        return Result.LOST
                    case Action.PAPER:
                        return Result.DRAW
                    case Action.SCISSORS:
                        return Result.WON
            case Action.SCISSORS:
                match reaction:
                    case Action.ROCK:
                        return Result.WON
                    case Action.PAPER:
                        return Result.LOST
                    case Action.SCISSORS:
                        return Result.DRAW
