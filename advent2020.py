import advent2020
import sys

if __name__ == "__main__":
    day_no = sys.argv[1]
    if int(day_no) > advent2020.MAX_DAY:
        print("That day ain't been done yet.")
        exit()

    solver = getattr(advent2020, f"solve_day{day_no}")

    with open(f"input/input{day_no}.txt") as input:
        print(f"Answer: {solver([s.rstrip() for s in input])}")
