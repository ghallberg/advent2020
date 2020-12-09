from itertools import combinations


def is_valid(code, index, preamble_size):
    pairs = list(combinations(code[index - preamble_size : index], 2))
    valid_values = [x + y for x, y in pairs]
    return code[index] in valid_values


def first_invalid(code, preamble_size):
    for i in range(preamble_size, len(code)-1):
        if not is_valid(code, i, preamble_size):
            return code[i]


def find_weakness(code, target):
    for i in range(len(code)):
        run = [code[i]]
        for j in code[i+1:]:
            run.append(j)
            if sum(run) == target:
                return min(run) + max(run)
            elif sum(run) > target:
                break






def solve(input):
    int_code = [int(x) for x in input]
    a1 = first_invalid(int_code, 25)
    a2 = find_weakness(int_code, a1)
    return(a1, a2)

