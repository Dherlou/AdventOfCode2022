#!/usr/bin/env python3

from elf_pair import ElfPair

if __name__ == '__main__':
    elf_pairs = ElfPair.load_all('4/input.txt')

    have_subsets = map(
        ElfPair.has_subset,
        elf_pairs
    )
    subset_sum = sum(have_subsets)
    print(f'1) {subset_sum} elf pairs have subsets!')

    have_overlaps = map(
        ElfPair.has_overlap,
        elf_pairs
    )
    overlap_sum = sum(have_overlaps)
    print(f'2) {overlap_sum} elf pairs have subsets!')
