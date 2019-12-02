# Advent Of Code 2019, Day 1, Part 2
# Author: Joth (https://github.com/joth00)

from math import floor


def calculateTotalFuelByMass(mass):
    def calculateFuelByMass(m): return floor(m/3) - 2

    fuel = calculateFuelByMass(mass)
    fuel_sum = 0

    while fuel > 0:
        fuel_sum += fuel
        fuel = calculateFuelByMass(fuel)

    return fuel_sum


masses = [int(x) for x in open('input.txt', 'r').read().splitlines()]
fuel_sum = 0
for mass in masses:
    fuel_sum += calculateTotalFuelByMass(mass)

print('Total fuel:', fuel_sum)
