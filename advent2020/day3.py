from itertools import cycle, count, islice
from functools import reduce
from operator import mul

path_steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def path_generator(input, x_step, y_step):
    slope = [cycle(line) for line in input]
    for row, x in zip(slope[y_step::y_step], count(start=x_step, step=x_step)):
        yield next(islice(row, x, None))


def count_trees(path):
    return list(path).count("#")


def solve(input):
    tree_counts = {
        (y, x): count_trees(path_generator(input, y, x)) for y, x in path_steps
    }
    return (tree_counts[(3, 1)], reduce(mul, tree_counts.values()))


if __name__ == "__main__":
    with open("../input/input3.txt") as input:
        solve(input)
