from itertools import takewhile, islice, chain

REQUIRED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

#I   byr (Birth Year)
#    iyr (Issue Year)
#    eyr (Expiration Year)
#    hgt (Height)
#    hcl (Hair Color)
#    ecl (Eye Color)
#    pid (Passport ID)
#    cid (Country ID)


def is_valid(passport):
    passport_keys = set(passport.keys())
    return passport_keys.issuperset(REQUIRED_KEYS)


def flatten(list_of_lists):
    return chain(*list_of_lists)


def make_passport(data):
    pair_strings = flatten([line.split() for line in data])
    pairs = [pair.split(":") for pair in pair_strings]

    return dict(pairs)


def not_empty(x):
    return x != ""


def passport_generator(lines):
    while len(lines) > 0:
        passport_data = list(takewhile(not_empty, lines))
        lines = list(islice(lines, len(passport_data) + 1, None))
        yield make_passport(passport_data)


def solve(input):
    parsed_input = [line.rstrip() for line in input]
    gen = passport_generator(parsed_input)
    return len(list([passport for passport in gen if is_valid(passport)]))

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
