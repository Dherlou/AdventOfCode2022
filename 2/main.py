#!/usr/bin/env python3

from game import Game
from strategy_guide import Strategy, StrategyGuide


if __name__ == '__main__':
    for idx, strategy in enumerate([Strategy.ACTION, Strategy.OUTCOME], 1):
        strategy_guide = StrategyGuide('2/input.txt', strategy)
        score = Game.play(strategy_guide)
        print(f'{idx}) Total score with Strategy={strategy.name}: {score}')
