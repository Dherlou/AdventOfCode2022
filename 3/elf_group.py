from __future__ import annotations

from rucksack import Rucksack


class ElfGroup:

    def __init__(self, rucksacks: list[Rucksack]):
        self.__rucksacks = rucksacks

    @classmethod
    def load_all(self, rucksacks: list[Rucksack], group_size: int = 3) -> list[ElfGroup]:
        elf_groups = []
        rucksack_count = len(rucksacks)

        for idx in range(0, rucksack_count, group_size):
            elf_groups.append(
                ElfGroup(rucksacks[idx:min(idx + group_size, rucksack_count)])
            )

        return elf_groups

    def find_badge(self) -> int:
        for priority in self.__rucksacks[0].get_content():
            if all(priority in rucksack.get_content() for rucksack in self.__rucksacks):
                return priority

        raise ValueError('Elf Group has no badge!')
