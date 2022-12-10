from __future__ import annotations
from collections import OrderedDict
from functools import reduce
import math
import re

from cranes import Crane
from movement import Movement


class StorageYard:

    def __init__(self, crates: dict[list[str]], crane: Crane):
        self.__crates = crates
        self.__crane = crane

    @classmethod
    def load_crates(self, input_file: str) -> dict[list[str]]:
        with open(input_file, 'r') as file:
            crates: dict[list[str]] = {}
            lines = [line.rstrip() for line in file]

            for line in lines:
                # find all (unique) crates of that line/height
                search = set(re.findall(r'\[([A-Z])\]', line))

                # for all (unique) crates of the current height ...
                for crate in search:
                    # ... find all stack positions
                    stacks = [math.ceil(p.start() / 4)
                              for p in re.finditer(crate, line)]

                    for stack in stacks:
                        if stack in crates:
                            crates[stack].insert(0, crate)
                        else:
                            crates[stack] = [crate]

            return crates

    def execute(self, movement: Movement) -> None:
        self.__crates = self.__crane.execute(self.__crates, movement)

    def get_top_crates(self) -> str:
        return reduce(
            lambda s1, s2: s1+s2,
            map(
                lambda crate_item: crate_item[1][-1],
                OrderedDict(sorted(self.__crates.items())).items()
            )
        )
