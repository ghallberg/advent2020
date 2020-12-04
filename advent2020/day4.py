from itertools import takewhile, islice, chain
import re

REQUIRED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

YR_RANGES = {"byr": (1920, 2002), "iyr": (2010, 2020), "eyr": (2020, 2030)}

HGT_PATTERN = re.compile(r"^(\d+)([a-z]+)$")
HGT_RANGES = {"cm": (150, 193), "in": (59,76)}

HCL_PATTERN = re.compile(r"^#[a-f0-9]{6}$")

ECL_VALUES = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

PID_PATTERN = re.compile(r"^\d{9}$")


def has_valid_values(passport):
    return all([validate_value(k,v) for k,v in passport.items()])


def validate_yr(key,value):
    min,max = YR_RANGES[key]
    return min <= int(value) <= max


def validate_hgt(value):
    match = HGT_PATTERN.match(value)
    if not match:
        return False

    value, unit = match.groups()
    min, max = HGT_RANGES[unit]
    return min <= int(value) <= max


def validate_hcl(value):
    return HCL_PATTERN.match(value)


def validate_ecl(value):
    return value in ECL_VALUES


def validate_pid(value):
    return PID_PATTERN.match(value) is not None


def validate_value(key, value):
    if key in ("byr", "iyr", "eyr"):
        return validate_yr(key,value)
    elif key == "hgt":
        return validate_hgt(value)
    elif key == "hcl":
        return validate_hcl(value)
    elif key == "ecl":
        return validate_ecl(value)
    elif key == "pid":
        return validate_pid(value)
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
    valid_value_passports = [passport for passport in valid_key_passports if has_valid_values(passport)]
    return (len(list(valid_key_passports)), len(list(valid_value_passports)))


if __name__ == "__main__":
    with open("../input/input4.txt") as input:
        solve(input)

    #    byr (Birth Year)
    #    iyr (Issue Year)
    #    eyr (Expiration Year)
    #    hgt (Height)
    #    hcl (Hair Color)
    #    ecl (Eye Color)
    #    pid (Passport ID)
    #    cid (Country ID)
