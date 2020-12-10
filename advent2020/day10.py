from functools import reduce
from operator import mul

from math import factorial


def parse_input(lines):
    int_lines = [int(line) for line in lines]
    int_lines.sort()
    return int_lines


def step_reducer(prev_steps, step_jolts):
    step_size = step_jolts - prev_steps[-1]["jolts"]
    prev_steps.append({"jolts": step_jolts, "size": step_size})
    return prev_steps

def run_reducer(runs, step):
    if step["size"] == 1:
        runs[-1] = runs[-1] + 1
    elif step["size"] == 3 and runs[-1] != 0:
        runs.append(0)

    return runs

def sum_ints(i):
    if i < 2:
        return i
    else:
        return i + sum_ints(i-1)



def variation_reducer(prod, run_size):
    multiplier = sum_ints(run_size-1) + 1
    if multiplier > 0:
        return prod*multiplier
    else:
        return prod


def solve(input):
    jolts = parse_input(input)
    jolts.append(max(jolts) + 3)
    first_step = {"jolts": jolts[0], "size": jolts[0]}
    steps = reduce(step_reducer, jolts[1:], [first_step])
    step_sizes = [step["size"] for step in steps]

    steps3 = len([size for size in step_sizes if size == 3])
    steps1 = len([size for size in step_sizes if size == 1])


    runs = reduce(run_reducer, steps, [0])

    print(runs)

    answer_guess = reduce(variation_reducer, runs, 1)


    return (steps3 * steps1, answer_guess)
