# Advent of Code 2019, Day 1, Part 2

from os import path
from math import floor


def calculate_total_fuel_by_mass(mass):
    calculate_fuel_by_mass = lambda m: floor(m/3) - 2

    fuel = calculate_fuel_by_mass(mass)
    fuel_sum = 0

    while fuel > 0:
        fuel_sum += fuel
        fuel = calculate_fuel_by_mass(fuel)

    return fuel_sum


def main():
    text_input = get_raw_input()
    masses = [int(x) for x in text_input.splitlines()]
    fuel_sum = 0
    for mass in masses:
        fuel_sum += calculate_total_fuel_by_mass(mass)

    print('Total fuel:', fuel_sum)


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


if __name__ == '__main__':
    main()
