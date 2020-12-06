from itertools import takewhile, islice
import string


def make_group(data):
    return {"members": data, "answers": set("".join(data))}


def group_generator(lines):
    while len(lines) > 0:
        group_data = list(takewhile(lambda x: x != "", lines))
        lines = list(islice(lines, len(group_data) + 1, None))
        yield make_group(group_data)


def num_all_answers(group):
    return [
        answer
        for answer in group["answers"]
        if all([answer in member for member in group["members"]])
    ]


def solve(input):
    groups = list(group_generator(input))
    sum_answers = sum([len(group["answers"]) for group in groups])
    sum_all_answers = sum([len(num_all_answers(group)) for group in groups])
    return (sum_answers, sum_all_answers)
