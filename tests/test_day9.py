import advent2020.day9 as d

test_code = [
    "35",
    "20",
    "15",
    "25",
    "47",
    "40",
    "62",
    "55",
    "65",
    "95",
    "102",
    "117",
    "150",
    "182",
    "127",
    "219",
    "299",
    "277",
    "309",
    "576",
]

int_test_code = [int(x) for x in test_code]


def test_is_valid():
    assert d.is_valid(int_test_code, 5, 5)
    assert not d.is_valid(int_test_code, 14, 5)


def test_first_invalid():
    assert d.first_invalid(int_test_code, 5) == 127


def test_find_weakness():
    assert d.find_weakness(int_test_code, 127) == 62
