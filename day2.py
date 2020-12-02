import re
CHECKER = re.compile(r"(\d+)-(\d+) (\w+): (\w.*)")

def tokenize(line):
    tokens =  CHECKER.match(line)
    pos1 = int(tokens[1])
    pos2 = int(tokens[2])
    char = tokens[3]
    password = tokens[4]

    return (pos1, pos2, char, password)

def is_valid(min_count, max_count, char, password):
    char_count = password.count(char)
    return min_count <= char_count <= max_count

def is_valid2(pos1, pos2, char, password):
    return (password[pos1-1] == char) != (password[pos2-1] == char)

def count_valid(candidates, validator):
    valid_candidates = [line for line in candidates if validator(*line)]
    return len(valid_candidates)

def solve(input):
    tokenized_input = [tokenize(line) for line in input]
    print(f"Answer 1: {count_valid(tokenized_input, is_valid)}")
    print(f"Answer 2: {count_valid(tokenized_input, is_valid2)}")


with open("input/input2.txt") as input:
    solve(input)

