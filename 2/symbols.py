from enum import Enum

class ActionSymbol(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'

class ReactionSymbol(Enum):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'

class OutcomeSymbol(Enum):
    LOST = 'X'
    DRAW = 'Y'
    WON = 'Z'