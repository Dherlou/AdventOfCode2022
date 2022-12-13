from __future__ import annotations
from itertools import chain


class GenericFile:

    def __init__(self, parent: Directory | None, name: str) -> None:
        self._parent = parent
        self._name = name

    def get_parent(self) -> Directory | None:
        return self._parent

    def get_name(self) -> str:
        return self._name

    def get_size(self) -> int:
        pass


class DistinctFile(GenericFile):

    def __init__(self, parent: Directory | None, name: str, size: int) -> None:
        super().__init__(parent, name)
        self.__size = size

    def get_size(self) -> int:
        return self.__size

    def set_size(self, size: int) -> None:
        self.__size = size

    def __repr__(self) -> str:
        return self.get_parent().__repr__() + f'/{self.get_name()} ({self.get_size()})'


class Directory(GenericFile):

    def __init__(self, parent: Directory | None, name: str) -> None:
        super().__init__(parent, name)
        self.__children: list[GenericFile] = []

    def get_children(self) -> list[GenericFile]:
        return self.__children

    def add_child(self, generic_file: GenericFile) -> None:
        self.__children.append(generic_file)

    def get_size(self) -> int:
        return sum(
            map(
                lambda f: f.get_size(),
                self.__children
            )
        ) if len(self.__children) > 0 else 0

    def walk_directories(self, p) -> list[GenericFile]:
        return [d for d in self.__children if isinstance(d, Directory) and p(d)] + \
            list(chain(*[d.walk_directories(p) for d in self.__children if isinstance(d, Directory)]))

    def __repr__(self) -> str:
        path = ''
        cwd = self

        while cwd is not None:
            path = f'{cwd.get_name()}/{path}'
            cwd = cwd.get_parent()

        return path + f' ({self.get_size()})'
