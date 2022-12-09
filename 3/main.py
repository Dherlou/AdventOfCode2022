#!/usr/bin/env python3

from elf_group import ElfGroup
from rucksack import Rucksack

if __name__ == '__main__':
    rucksacks = Rucksack.load_all('3/input.txt')

    duplicates = map(
        Rucksack.find_duplicates,
        rucksacks
    )
    priority_sum = sum(sum(dups) for dups in duplicates)
    print(f'1) The sum of all duplicate rucksack items is {priority_sum}!')

    elf_groups = ElfGroup.load_all(rucksacks)
    badges = map(
        ElfGroup.find_badge,
        elf_groups
    )
    badge_sum = sum(badges)
    print(f'2) The sum of the elf-group badges\' priorities is {badge_sum}!')
