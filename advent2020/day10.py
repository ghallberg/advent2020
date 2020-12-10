from functools import reduce


def parse_input(lines):
    int_lines = [int(line) for line in lines]
    int_lines.sort()
    return int_lines


def step_reducer(prev_steps, step_jolts):
    step_size = step_jolts - prev_steps[-1]["jolts"]
    prev_steps.append({"jolts": step_jolts, "size": step_size})
    return prev_steps


def solve(input):
    jolts = parse_input(input)
    jolts.append(max(jolts) + 3)
    first_step = {"jolts": jolts[0], "size": jolts[0]}
    steps = reduce(step_reducer, jolts[1:], [first_step])
    step_sizes = [step["size"] for step in steps]

    steps3 = len([size for size in step_sizes if size == 3])
    steps1 = len([size for size in step_sizes if size == 1])

    return (steps3 * steps1, None)
