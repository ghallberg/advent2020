from advent2020 import day7 as d

tinput2 = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags." ]

tinput = [
    "faded blue bags contain 2 dotted black bags.",
    "velvet red bags contain 5 faded blue bags, 1 dotted black bag.",
    "dotted black bags contain no other bags.",
]

trules = [('faded blue', [(2, 'dotted black')]),('velvet red', [(5, 'faded blue'), (1, 'dotted black')]),('dotted black', [])]


tgraph = {
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
    assert d.parse_rules(tinput) == trules

def test_make_graph():
    assert d.build_graph(trules) == tgraph

def test_calculate_contained_in():
    assert len(d.calculate_contained_in("velvet red", tgraph)) == 0
    assert len(d.calculate_contained_in("faded blue", tgraph)) == 1
    assert len(d.calculate_contained_in("dotted black", tgraph)) == 2

def test_solve():
    assert d.solve(tinput2) == (4, None)
