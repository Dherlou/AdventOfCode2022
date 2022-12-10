from movement import Movement


class Crane:
    def execute(self, crates: dict[list[str]], movement: Movement) -> dict[list[str]]:
        pass


class Crane9000(Crane):
    def execute(self, crates: dict[list[str]], movement: Movement) -> dict[list[str]]:
        for _ in range(movement.amount): # execute one-by-one
            moved_crate = crates[movement.src].pop()  # get and remove crate from old stack
            crates.setdefault(movement.dest, []).append(moved_crate)  # add to new stack
        return crates


class Crane9001(Crane):
    def execute(self, crates: dict[list[str]], movement: Movement) -> dict[list[str]]:
        moved_crates = crates[movement.src][-movement.amount:]  # get all crates at once
        del crates[movement.src][-movement.amount:]  # remove these crates from old stack
        crates.setdefault(movement.dest, []).extend(moved_crates)  # add these crates to new stack
        return crates
