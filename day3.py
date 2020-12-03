from itertools import cycle, count, islice
from functools import reduce
from operator import mul

path_steps = [(3,1),
              (1,1),
              (5,1),
              (7,1),
              (1,2)]

def path_generator(input, x_step, y_step):
    slope = [cycle(line) for line in input]

    for y,x,i in zip(range(y_step, len(slope), y_step), count(start=x_step, step=x_step), count(1)):
        x_content = slope[y]
        yield next(islice(x_content, i*x_step, None))

def count_trees(path):
    return list(path).count('#')

def solve(input):
    tree_counts = [count_trees(path_generator(input, y, x)) for y,x in path_steps]
    print(f"Answer 1: {tree_counts[0]}")
    print(f"Answer 2: {reduce(mul, tree_counts)}")



with open("input/input3.txt") as real_input:
    solve([line.rstrip() for line in real_input])




