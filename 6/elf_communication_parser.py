class ElfCommunicationParser:

    @classmethod
    def get_first_marker_end_index(self, input_file: str, marker_length: int) -> int:
        with open(input_file, 'r') as file:
            idx = 0
            lookback: list[str] = []

            while True:
                idx += 1
                char = file.read(1)

                if not char:
                    raise EOFError('Marker not found!')

                if len(lookback) < marker_length:
                    lookback.append(char)
                    continue

                lookback.pop(0)
                lookback.append(char)

                if len(lookback) == len(set(lookback)):
                    return idx
