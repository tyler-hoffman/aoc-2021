from typing import List
from src.day_03.shared import array_to_int, parse
from src.utils.collections import frequency_map


def get_gamma_bits(lines: List[str]) -> List[str]:
    line_len = len(lines[0])
    output: List[str] = []
    for index in range(line_len):
        freqs = frequency_map([line[index] for line in lines])
        zero_count = freqs.get("0", 0)
        one_count = freqs.get("1", 0)

        if zero_count > one_count:
            output.append("0")
        elif one_count > zero_count:
            output.append("1")
        else:
            raise Exception(f"Unknown winner at index {index}")
    return output

def inverse_bits(bits: List[str]) -> List[str]:
    return ["0" if bit == "1" else "1" for bit in bits]

def solve(input: str) -> int:
    lines = parse(input)

    gamma_bits = get_gamma_bits(lines)
    epsilon_bits = inverse_bits(gamma_bits)


    return array_to_int(gamma_bits) * array_to_int(epsilon_bits)


if __name__ == "__main__":
    with open("src/day_03/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
