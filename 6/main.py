#!/usr/bin/env python3

from elf_communication_parser import ElfCommunicationParser


if __name__ == '__main__':
    marker_lengths = {
        'packet': 4,
        'message': 14
    }

    for idx, (marker_type, marker_length) in enumerate(marker_lengths.items()):
        first_marker_end_idx = ElfCommunicationParser.get_first_marker_end_index(
            '6/input.txt', marker_length)
        print(f'{idx}) First {marker_type} marker end index is {first_marker_end_idx}!')
