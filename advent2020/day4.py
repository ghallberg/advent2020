from itertools import takewhile, islice, chain
import re

REQUIRED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

def str_range(start, stop):
    return [str(num) for num in range(start, stop)]

ALLOWED_VALS = {
    "byr": str_range(1920, 2003),
    "iyr": str_range(2010, 2021),
    "eyr": str_range(2020, 2031),
    "ecl": ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "cm": str_range(150, 194),
    "in": str_range(59, 77),
}
PATTERNS = {
    "hgt": re.compile(r"(\d+)([a-z]+)"),
    "hcl": re.compile(r"#[a-f0-9]{6}"),
    "pid": re.compile(r"\d{9}"),
}


def has_valid_values(passport):
    return all([validate_value(k, v) for k, v in passport.items()])


def is_allowed(key, value):
    return value in ALLOWED_VALS[key]


def valid_pattern_match(key, value):
    return PATTERNS[key].match(value)


def validate_value(key, value):
    if key in ("byr", "iyr", "eyr", "ecl"):
        return is_allowed(key, value)
    elif key in ("hcl", "pid"):
        return valid_pattern_match(key, value)
    elif key == "hgt":
        match = valid_pattern_match("hgt", value)
        return is_allowed(match[2], match[1]) if match else False
    else:
        return True


def flatten(list_of_lists):
    return chain(*list_of_lists)


def has_valid_keys(passport):
    passport_keys = set(passport.keys())
    return passport_keys.issuperset(REQUIRED_KEYS)


def make_passport(data):
    pair_strings = flatten([line.split() for line in data])
    pairs = [pair.split(":") for pair in pair_strings]

    return dict(pairs)


def passport_generator(lines):
    while len(lines) > 0:
        passport_data = list(takewhile(lambda x: x != "", lines))
        lines = list(islice(lines, len(passport_data) + 1, None))
        yield make_passport(passport_data)


def solve(input):
    parsed_input = [line.rstrip() for line in input]
    gen = passport_generator(parsed_input)
    valid_key_passports = [passport for passport in gen if has_valid_keys(passport)]
    valid_value_passports = [
        passport for passport in valid_key_passports if has_valid_values(passport)
    ]
    return (len(list(valid_key_passports)), len(list(valid_value_passports)))


if __name__ == "__main__":
    with open("../input/input4.txt") as input:
        solve(input)
