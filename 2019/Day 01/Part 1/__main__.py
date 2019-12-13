# Advent of Code 2019, Day 1, Part 1

from os import path
from math import floor


def main():
    text_input = get_raw_input()
    masses = [int(x) for x in text_input.splitlines()]

    fuel_sum = 0
    for mass in masses:
        fuel_sum += floor(mass/3) - 2

    print('Total fuel:', fuel_sum)


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


if __name__ == '__main__':
    main()