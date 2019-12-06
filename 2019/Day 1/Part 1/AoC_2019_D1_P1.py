# Advent Of Code 2019, Day 1, Part 1
# Author: Joth (https://github.com/joth00)

from math import floor

masses = [int(x) for x in open('input.txt', 'r').read().splitlines()]
fuel_sum = 0
for mass in masses:
    fuel_sum += floor(mass/3) - 2

print('Total fuel:', fuel_sum)
