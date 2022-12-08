from __future__ import annotations
from enum import Enum

from symbols import OutcomeSymbol


class ResultData:
    def __init__(self, symbol: str, score: int):
        self.__symbol = symbol
        self.__score = score

    @property
    def symbol(self):
        return self.__symbol

    @property
    def score(self):
        return self.__score


class Result(Enum):
    LOST = ResultData(OutcomeSymbol.LOST.value, 0)
    DRAW = ResultData(OutcomeSymbol.DRAW.value, 3)
    WON = ResultData(OutcomeSymbol.WON.value, 6)
