from __future__ import annotations
import re
from typing import Tuple

from files import GenericFile, DistinctFile, Directory


class ConsoleParser:

    @classmethod
    def parse(self, input_file: str) -> GenericFile:
        with open(input_file, 'r') as file:
            history = [line.strip() for line in file]
            root = Directory(None, '/')
            cwd = root

            while True:
                if len(history) == 0:
                    break

                history, cwd = self.execute_cmd(history, cwd)

            return root

    @classmethod
    def execute_cmd(self, history: list[str], cwd: Directory) -> Tuple[list[str], Directory]:
        cmd = history.pop(0)

        cmd_cd = re.search('\$ cd (\w+|\.\.|\/)', cmd)
        cmd_ls = re.search('ls', cmd)
        if cmd_cd is not None:
            cwd = self.execute_cmd_cd(cwd, cmd_cd.group(1))
        elif cmd_ls is not None:
            history, cwd = self.execute_cmd_ls(history, cwd)
        else:
            raise ValueError(f'Unknown history entry: {cmd}')

        return (history, cwd)

    @classmethod
    def execute_cmd_cd(self, cwd: Directory, cd: str) -> Directory:
        if cd == '..':
            if cwd.get_parent() != None:
                cwd = cwd.get_parent()
        elif cd == '/':
            while True:
                parent = self.execute_cmd_cd(cwd, '..')
                if cwd == parent:
                    break
                cwd = parent
        else:
            found = False
            for child in cwd.get_children():
                if child.get_name() == cd:
                    cwd = child
                    found = True
                    break
            if not found:
                child = Directory(cwd, cd)
                cwd.add_child(child)
                cwd = child

        return cwd

    @classmethod
    def execute_cmd_ls(self, history: list[str], cwd: Directory) -> Tuple[list[str], Directory]:
        while len(history) > 0 and not history[0].startswith('$'):
            ls = history.pop(0)

            ls_file = re.search('(\d+) ([\w\.]+)', ls)
            ls_dir = re.search('dir (\w+)', ls)
            if ls_file is not None:
                found = False
                for child in cwd.get_children():
                    if child.get_name() == ls_file.group(2) and isinstance(child, DistinctFile):
                        child.set_size(int(ls_file.group(1)))
                        found = True
                        break
                if not found:
                    child = DistinctFile(
                        cwd, ls_file.group(2), int(ls_file.group(1)))
                    cwd.add_child(child)
            elif ls_dir is not None:
                found = False
                for child in cwd.get_children():
                    if child.get_name() == ls_dir.group(1) and isinstance(child, Directory):
                        found = True
                        break
                if not found:
                    child = Directory(cwd, ls_dir.group(1))
                    cwd.add_child(child)
            else:
                raise ValueError(f'Unknown ls entry: {ls}')

        return (history, cwd)
