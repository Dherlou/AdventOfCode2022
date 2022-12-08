from duel import Duel
from strategy_guide import StrategyGuide


class Game:

    @classmethod
    def play(self, strategy_guide: StrategyGuide) -> int:
        return sum(
            map(
                lambda duel: Duel.play(duel[0], duel[1]),
                strategy_guide.guide
            )
        )
