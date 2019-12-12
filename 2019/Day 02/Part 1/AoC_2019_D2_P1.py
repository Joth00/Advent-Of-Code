# Advent of Code 2019, Day 2, Part 1
# Author: Joth (https://github.com/joth00)

from os import path


def main():
    text_input = get_raw_input()
    int_code = [int(x) for x in text_input.split(',')]

    int_code[1] = 12
    int_code[2] = 2

    i = 0
    while i < len(int_code):
        opcode = int_code[i]
        if opcode == 1:
            int_code[int_code[i+3]] = int_code[int_code[i+1]] + int_code[int_code[i+2]]
        elif opcode == 2:
            int_code[int_code[i+3]] = int_code[int_code[i+1]] * int_code[int_code[i+2]]
        elif opcode == 99:
            break
        i += 4

    print(int_code[0])


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
