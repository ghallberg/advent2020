from advent2020.day4 import solve, passport_generator, make_passport


def test_gen():
    input = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
        "hcl:#cfa07d byr:1929",
        "",
        "hcl:#ae17e1 iyr:2013",
        "eyr:2024",
        "ecl:brn pid:760753108 byr:1931",
        "hgt:179cm",
        "",
        "hcl:#cfa07d eyr:2025 pid:166559648",
        "iyr:2011 ecl:brn hgt:59in",
    ]

    g = passport_generator(input)
    assert next(g) == {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    }
    assert next(g) == {
        "iyr": "2013",
        "ecl": "amb",
        "cid": "350",
        "eyr": "2023",
        "pid": "028048884",
        "hcl": "#cfa07d",
        "byr": "1929",
    }

    assert next(g) == {
        "hcl": "#ae17e1",
        "iyr": "2013",
        "eyr": "2024",
        "ecl": "brn",
        "pid": "760753108",
        "byr": "1931",
        "hgt": "179cm",
    }

    assert next(g) == {
        "hcl": "#cfa07d",
        "eyr": "2025",
        "pid": "166559648",
        "iyr": "2011",
        "ecl": "brn",
        "hgt": "59in",
    }


def test_make_passport():
    input = ["hej:san då:sig", "la:di da:da"]

    assert make_passport(input) == {"hej": "san", "då": "sig", "la": "di", "da": "da"}


def test_solve():
    input = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
        "hcl:#cfa07d byr:1929",
        "",
        "hcl:#ae17e1 iyr:2013",
        "eyr:2024",
        "ecl:brn pid:760753108 byr:1931",
        "hgt:179cm",
        "",
        "hcl:#cfa07d eyr:2025 pid:166559648",
        "iyr:2011 ecl:brn hgt:59in",
    ]

    assert solve(input) == (2, 2)
