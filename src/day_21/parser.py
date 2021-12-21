class Parser(object):
    @staticmethod
    def parse(input: str) -> tuple[int, int]:
        lines = input.strip().splitlines()
        assert len(lines) == 2

        last_word_of_lines = [line.split()[-1] for line in lines]
        return tuple([int(x) - 1 for x in last_word_of_lines])
