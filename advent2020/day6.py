from itertools import takewhile, islice
import string

test_data = ["abc", "", "a", "b", "c", "", "ab", "ac", "", "a", "a", "a", "a", "", "b"]


def make_group(data):
    return {"members": data, "answers": set("".join(data))}


def group_generator(lines):
    while len(lines) > 0:
        group_data = list(takewhile(lambda x: x != "", lines))
        lines = list(islice(lines, len(group_data) + 1, None))
        yield make_group(group_data)


def solve(input):
    groups = group_generator(input)
    sum_answers = sum([len(group["answers"]) for group in groups])
    return (sum_answers, None)
