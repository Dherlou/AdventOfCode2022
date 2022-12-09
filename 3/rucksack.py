from __future__ import annotations


class Rucksack:

    def __init__(self, comp1: list[int], comp2: list[int]):
        self.__comp1 = comp1
        self.__comp2 = comp2

    @classmethod
    def load_all(self, input_file: str) -> list[Rucksack]:
        with open(input_file, 'r') as file:
            lines = [line.strip() for line in file]
            return list(
                map(
                    lambda line: self.parse(line),
                    lines
                )
            )

    @classmethod
    def parse(self, raw_content: str) -> Rucksack:
        full_content: list[int] = []

        for item_str in raw_content:
            ascii = ord(item_str)
            if ord('A') <= ascii and ascii <= ord('Z'):
                ascii -= 38  # ascii -> priority
            elif ord('a') <= ascii and ascii <= ord('z'):
                ascii -= 96  # ascii -> priority
            else:
                raise ValueError(f'Unknown rucksack content: {item_str}!')
            full_content.append(ascii)

        comp_divider = int(len(raw_content) / 2)
        return Rucksack(full_content[:comp_divider], full_content[comp_divider:])

    def get_content(self) -> list[int]:
        return self.__comp1 + self.__comp2

    def find_duplicates(self) -> list[int]:
        duplicates: set = set()

        for priority in self.__comp1:
            if priority in self.__comp2:
                duplicates.add(priority)

        return duplicates
