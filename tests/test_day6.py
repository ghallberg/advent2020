import advent2020.day6 as day6

test_data = ["abc", "", "a", "b", "c", "", "ab", "ac", "", "a", "a", "a", "a", "", "b"]


def test_solve():
    assert day6.solve(test_data) == (11, 6)
