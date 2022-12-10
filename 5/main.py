#!/usr/bin/env python3

from cranes import Crane9000, Crane9001
from movement import Movement
from storage_yard import StorageYard


if __name__ == '__main__':
    input_file = '5/input.txt'
    movements = Movement.load_all(input_file)

    for idx, crane in enumerate([Crane9000(), Crane9001()], 1):
        crates = StorageYard.load_crates(input_file)
        storage_yard = StorageYard(crates, crane)

        for movement in movements:
            storage_yard.execute(movement)

        top_crates = storage_yard.get_top_crates()
        print(f'{idx}) The top crates have the order {top_crates}!')
