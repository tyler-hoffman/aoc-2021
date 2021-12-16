def hex_to_binary(hex_number: str) -> str:
    numbers = [int(x, 16) for x in hex_number]
    array_of_bits = [f"{x:>04b}" for x in numbers]
    all_bits = "".join(array_of_bits)
    # output = strip_trailing_zeroes(all_bits)

    return all_bits


def strip_trailing_zeroes(bits: str) -> str:
    reversed = bits[::-1]
    to_skip = reversed.index("1")
    return bits[:-to_skip]
