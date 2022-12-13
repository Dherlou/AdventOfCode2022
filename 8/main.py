#!/usr/bin/env python3

from forest import Forest


if __name__ == '__main__':
    grid: list[list[int]] = Forest.parse('8/input.txt')
    
    #1
    visible_trees = Forest.get_number_visible_trees(grid)
    print(f'1) {visible_trees} trees are visible!')

    #2
    best_scenic_score = Forest.get_best_scenic_score(grid)
    print(f'2) The highest possible scenic score is {best_scenic_score}!')