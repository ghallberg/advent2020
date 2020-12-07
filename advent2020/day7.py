import re
from functools import reduce
from itertools import chain

CONTAINER_PATTERN = re.compile(r"([\w\s]+?) bags contain (.+?)\.$")
CONTENT_PATTERN = re.compile(r"(\d) (.+?) bag(?:s|)")


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
        graph[container_name]["contains"][name] = amount
        graph[name]["contained_in"][container_name] = amount
    return graph


def empty_graph(rules):
    return {rule[0]: {"contains": {}, "contained_in": {}} for rule in rules}


def calculate_contained_in(color, graph):
    parents = set(graph[color]["contained_in"].keys())
    if parents:
        further_parents = list(
            chain(*[calculate_contained_in(color, graph) for color in parents])
        )
        if further_parents:
            parents.update(further_parents)
            return parents

    return parents


def parse_rules(input):
    return [parse_line(line) for line in input]


def build_graph(rules):
    return reduce(add_to_graph, rules, empty_graph(rules))


def solve(input):
    rules = parse_rules(input)
    graph = build_graph(rules)
    return (len(calculate_contained_in("shiny gold", graph)), None)
