# Advent Of Code 2019, Day 2, Part 2
# Author: Joth (https://github.com/joth00)

from os import path


def main():
    text_input = get_raw_input()
    int_code = [int(x) for x in text_input.split(',')]

    expected_output = 19690720

    noun_guess = 0
    verb_guess = 0

    output = 0
    for noun_guess in range(100):
        for verb_guess in range(100):
            output = get_int_code_output(int_code, noun_guess, verb_guess)
            if output is not None and output == expected_output:
                print(output, noun_guess, verb_guess, 100*noun_guess + verb_guess)
                return


def get_int_code_output(int_code_, noun, verb):
    int_code = int_code_[:]
    
    int_code[1] = noun
    int_code[2] = verb

    i = 0
    while i < len(int_code):
        opcode = int_code[i]
        if opcode == 1:
            int_code[int_code[i+3]] = int_code[int_code[i+1]] + int_code[int_code[i+2]]
        elif opcode == 2:
            int_code[int_code[i+3]] = int_code[int_code[i+1]] * int_code[int_code[i+2]]
        elif opcode == 99:
            break
        else:
            # print('something went wrong')
            return None
        i += 4
    
    return int_code[0]


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
