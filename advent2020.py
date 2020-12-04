import advent2020
import sys

if __name__ == "__main__":
    day_no = sys.argv[1]
    solver = getattr(advent2020, f"solve_day{day_no}")

    with open(f"input/input{day_no}.txt") as input:
        solver(input)
