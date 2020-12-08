def parse_instruction(line):
    instruction, step = line.split()
    return (instruction, int(step))


def parse_program(lines):
    return [parse_instruction(line) for line in lines]


def gen_alt_programs(program):
    for i in range(len(program)):
        ins, step = program[i]
        if ins == "jmp":
            new_ins = "nop"
        elif ins == "nop":
            new_ins = "jmp"
        else:
            new_ins = "acc"

        p2 = program[:]
        p2[i] = (new_ins, step)
        yield p2


def perform_instruction(program, i, acc):
    ins, step = program[i]
    if ins == "acc":
        acc = acc + step

    if ins == "jmp":
        i = i + step
    else:
        i = i + 1

    return i, acc


def run_until_loop_or_end(program):
    i = 0
    acc = 0
    seen_is = []
    while (i not in seen_is) and i < len(program):
        seen_is.append(i)
        i, acc = perform_instruction(program, i, acc)

    return acc, i


def solve(input):
    program = parse_program(input)
    alt_p = gen_alt_programs(program)
    for prog in alt_p:
        acc, last_ins = run_until_loop_or_end(prog)
        if last_ins >= len(program):
            break

    return (run_until_loop_or_end(program), acc)
