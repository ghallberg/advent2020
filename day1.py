from itertools import combinations
from functools import reduce
from operator import mul

def is_match(num_group):
    return sum(num_group) == 2020

def get_match(nums, group_size):
    groups = combinations(nums, group_size)
    return next(reduce(mul, group) for group in groups if is_match(group))


with open('input1.txt') as input:
   nums = [int(line) for line in input]

   result1 = get_match(nums, 2)
   result2 = get_match(nums, 3)

   print(f"Answer1: {result1}, Answer2: {result2}")
