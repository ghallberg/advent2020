import re

CHECKER = re.compile(r"(\d+)-(\d+) (\w+): (\w.*)")


def tokenize(line):
    tokens = CHECKER.match(line)
    pos1 = int(tokens[1])
    pos2 = int(tokens[2])
    char = tokens[3]
    password = tokens[4]

    return (pos1, pos2, char, password)


def valid_sled(min_count, max_count, char, password):
    char_count = password.count(char)
    return min_count <= char_count <= max_count


def valid_tobogan(pos1, pos2, char, password):
    return (password[pos1 - 1] == char) != (password[pos2 - 1] == char)


def count_valid(candidates, validator):
    valid_candidates = [line for line in candidates if validator(*line)]
    return len(valid_candidates)


def solve(input):
    tokenized_input = [tokenize(line) for line in input]
    res1 = count_valid(tokenized_input, valid_sled)
    res2 = count_valid(tokenized_input, valid_tobogan)

    return (res1, res2)


if __name__ == "__main__":
    with open("../input/input2.txt") as input:
        solve(input)
