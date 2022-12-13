#!/usr/bin/env python3

from console_parser import ConsoleParser
from files import Directory


if __name__ == '__main__':
    filetree: Directory = ConsoleParser.parse('7/input.txt')

    # 1
    small_files_size = sum(list(map(
        lambda f: f.get_size(),
        filetree.walk_directories(
            lambda d: d.get_size() <= 100_000
        )
    )))
    print(f'1) File size sum of files with size <= 100_000 is {small_files_size}!')
    
    #2
    free_space_current = 70_000_000 - filetree.get_size()
    free_space_missing = 30_000_000 - free_space_current
    deletion_sizes = map(
        lambda f: f.get_size(),
        filetree.walk_directories(
            lambda d: free_space_missing <= d.get_size()
        )
    )
    deletion_size = min(deletion_sizes)
    print(f'2) File size of the smallest directory after whose deletion the required disk space is available: {deletion_size}!')
