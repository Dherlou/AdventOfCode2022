from __future__ import annotations
import re


class ElfPair:

    def __init__(self, elf1: set[int], elf2: set[int]):
        self.__elf1 = elf1
        self.__elf2 = elf2

    @classmethod
    def load_all(self, input_file: str) -> list[ElfPair]:
        with open(input_file, 'r') as file:
            elf_pairs = []
            lines = [line.strip() for line in file]

            for line in lines:
                s = re.search('(\d+)-(\d+),(\d+)-(\d+)', line, re.IGNORECASE)
                elf_pair = ElfPair(
                    set(range(int(s.group(1)), int(s.group(2))+1)),
                    set(range(int(s.group(3)), int(s.group(4))+1))
                )
                elf_pairs.append(elf_pair)

            return elf_pairs

    def has_subset(self) -> bool:
        return self.__elf1.issubset(self.__elf2) or \
            self.__elf2.issubset(self.__elf1)

    def has_overlap(self) -> bool:
        return not self.__elf1.isdisjoint(self.__elf2) or \
            not self.__elf2.isdisjoint(self.__elf1)
