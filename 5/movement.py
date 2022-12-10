from __future__ import annotations
import re


class Movement:

    def __init__(self, src: int, dest: int, amount: int = 1) -> None:
        self.src = src
        self.dest = dest
        self.amount = amount

    @classmethod
    def load_all(self, input_file: str) -> list[Movement]:
        with open(input_file, 'r') as file:
            movements: list[Movement] = []
            lines = [line.strip() for line in file]

            for line in lines:
                s = re.search('move (\d+) from (\d+) to (\d+)',
                              line, re.IGNORECASE)

                if s is None:
                    continue

                movements.append(Movement(
                    int(s.group(2)),
                    int(s.group(3)),
                    int(s.group(1))
                ))

            return movements
