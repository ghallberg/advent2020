import advent2020.day8 as d

small_input = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6",
]


def test_solve():
    assert d.solve(small_input) == (5, None)
