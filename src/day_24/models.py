from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Module(object):
    """Simulates a chunk of logic from the input file.

    The input file is essentially 18 lines repeated 14 times
    with a few small tweaks each time. The "z" variable
    is the only variable that really carries through to
    the next "module"; at the start of each, we pull w
    from input, then clear x and y.

    Here's the breakdown:
    inp w
    mul x 0
    add x z
    mod x 26
    div z 1    # the `1` here varies. Call it `a`
    add x 10   # the `10` here varies. Call it `b`
    eql x w
    eql x 0
    mul y 0
    add y 25
    mul y x
    add y 1
    mul z y
    mul y 0
    add y w
    add y 10   # the `10` here varies. Call it `c`
    mul y x
    add z y
    """

    a: int
    b: int
    c: int

    def new_z_for_w(self, z: int, w: int) -> int:
        """For a given z and value w will get,
        execute the above lines of code.
        """
        x = int(w != self.b + z % 26)
        y1 = 25 * x + 1
        y2 = (w + self.c) * x
        return (z // self.a) * y1 + y2

    def ws_to_output_zs(
        self, z: int, ws_to_check_in_order: list[int]
    ) -> dict[int, int]:
        """Computes a mapping of input w -> z without duplicate zs

        if 2 ws produce the same z, we pick the larger w
        """
        outputs_to_high_w = dict[int, int]()
        for w in ws_to_check_in_order:
            output_z = self.new_z_for_w(z, w)
            outputs_to_high_w[output_z] = w

        return {w: z for z, w in outputs_to_high_w.items()}
