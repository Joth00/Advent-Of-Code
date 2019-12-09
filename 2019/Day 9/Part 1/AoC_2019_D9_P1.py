# Advent of Code 2019, Day 9, Part 1
# Author: Joth (https://github.com/joth00)

from os import path
from intcode import IntCode


def main():
    text_input = get_raw_input()
    int_code = IntCode(text_input)

    int_code.add_input(1)
    int_code.execute()


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
