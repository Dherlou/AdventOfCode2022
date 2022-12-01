#!/usr/bin/env python3

def read_calories_input(input_file: str) -> list[str]:
    with open(input_file, 'r') as file:
        return [line.strip() for line in file]

def build_calories_statistics(calories_input: list[str]) -> dict[int, int]:
    calories: dict[int, int] = {}
    elf: int = 1

    for line in calories_input:
        if line:
            calories[elf] = int(line) + calories.get(elf, 0)
        else:
            elf += 1
    
    return calories

def determine_top_3_elfs(calories_statistics: dict[int, int]) -> list[int]:
    return sorted(calories_statistics, key=calories_statistics.get, reverse=True)[:3]

if __name__ == '__main__':
    calories_input = read_calories_input('1/input.txt')
    calories_statistics = build_calories_statistics(calories_input)
    elf_top_3 = determine_top_3_elfs(calories_statistics)
    
    print(f'1) Elf {elf_top_3[0]} has the most calories with an amount of {calories_statistics[elf_top_3[0]]:,}!')
    print(f'2) The top 3 elfs have a total of {sum(map(calories_statistics.get, elf_top_3)):,} calories together!')
