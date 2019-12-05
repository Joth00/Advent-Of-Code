# Advent Of Code 2019, Day 6, Part 1
# Author: Joth (https://github.com/joth00)

from os import path


def main():
    text_input = get_raw_input()
    pass


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
