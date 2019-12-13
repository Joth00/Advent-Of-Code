# Advent of Code 2019, Day 13, Part 1

from os import path
from intcode import IntCode


def main():
    text_input = get_raw_input()
    int_code = IntCode(text_input)
    
    int_code.execute_till_halt()
    
    output_instructions = list(int_code.output_buffer.queue)
    tiles = dict()
    i = 0
    while i + 2 < len(output_instructions):
        tiles[(output_instructions[i], output_instructions[i + 1])] = output_instructions[i + 2]
        i += 3
    
    count = 0
    for tile in tiles.values():
        if tile == 2:
            count += 1
    
    print(count)


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


if __name__ == '__main__':
    main()