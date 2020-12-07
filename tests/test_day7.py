from advent2020 import day7 as d

test_input_1 = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]

test_input_2 = [
    "shiny gold bags contain 2 dark red bags.",
    "dark red bags contain 2 dark orange bags.",
    "dark orange bags contain 2 dark yellow bags.",
    "dark yellow bags contain 2 dark green bags.,",
    "dark green bags contain 2 dark blue bags.",
    "dark blue bags contain 2 dark violet bags.",
    "dark violet bags contain no other bags.",
]


small_input = [
    "faded blue bags contain 2 dotted black bags.",
    "velvet red bags contain 5 faded blue bags, 1 dotted black bag.",
    "dotted black bags contain no other bags.",
]

small_rules = [
    ("faded blue", [(2, "dotted black")]),
    ("velvet red", [(5, "faded blue"), (1, "dotted black")]),
    ("dotted black", []),
]


small_graph = {
    "faded blue": {"contained_in": {"velvet red": 5}, "contains": {"dotted black": 2}},
    "velvet red": {
        "contained_in": {},
        "contains": {"faded blue": 5, "dotted black": 1},
    },
    "dotted black": {
        "contained_in": {"faded blue": 2, "velvet red": 1},
        "contains": {},
    },
}


def test_parse_line():
    assert d.parse_rules(small_input) == small_rules


def test_make_graph():
    assert d.build_graph(small_rules) == small_graph


def test_calculate_contained_in():
    assert len(d.calculate_contained_in("velvet red", small_graph)) == 0
    assert len(d.calculate_contained_in("faded blue", small_graph)) == 1
    assert len(d.calculate_contained_in("dotted black", small_graph)) == 2


def test_solve():
    assert d.solve(test_input_1) == (4, None)
