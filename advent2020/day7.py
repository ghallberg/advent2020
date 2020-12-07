{
    "faded blue": {"contained_in": {"velvet red": 5}, "contains": {"dotted black": 2}},
    "velvet red": {
        "contained_in": [],
        "contains": {"faded blue": 5, "dotted black": 1},
    },
    "dotted black": {
        "contained_in": {"faded blue": 2, "velvet red": 1},
        "contains": [],
    },
}

import re
from functools import reduce

CONTAINER_PATTERN = re.compile(r"([\w\s]+?) bags contain (.+?)\.$")
CONTENT_PATTERN = re.compile(r"(\d) (.+?) bag(?:s|)")

tinput = [
    "faded blue bags contain 2 dotted black bags.",
    "velvet red bags contain 5 faded blue bags, 1 dotted black bag.",
    "dotted black bags contain no other bags.",
]


def content_gen(contents):
    for content in [CONTENT_PATTERN.match(s.strip()) for s in contents.split(",")]:
        if not content:
            break
        yield content.groups()


def parse_line(line):
    container, contents = CONTAINER_PATTERN.match(line).groups()
    return container, [(int(amount), type) for amount, type in content_gen(contents)]


def add_to_graph(graph, rule):
    container_name, contents = rule
    for amount, name in contents:
        print(f"Amount: {amount}, Name: {name}")
        graph[container_name]["contains"][name] = amount
        graph[name]["contained_in"][container_name] = amount
    return graph


def empty_graph(rules):
    return {rule[0]: {"contains": {}, "contained_in": {}} for rule in rules}


def calculate_contained_in(color, graph, containers=set()):
    contained_in = graph[color]["contained_in"].keys()
    if contained_in:
        return set(contained_in).update(
    else:
        return []


def solve(input):
    rules = [parse_line(line) for line in input]
    graph = reduce(add_to_graph, rules, empty_graph(rules))
    return (calculate_contained_in("shiny gold", graph), None)
