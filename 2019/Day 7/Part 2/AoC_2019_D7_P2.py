# Advent of Code 2019, Day 7, Part 2
# Author: Joth (https://github.com/joth00)

from os import path
from amplifier import Amplifier

def main():
    text_input = get_raw_input()
    amplifier_controller_software = [int(x) for x in text_input.split(',')]
    phase_settings = [5, 6, 7, 8, 9]

    amplifiers = []
    for _ in range(len(phase_settings)):
        amplifiers.append(Amplifier(amplifier_controller_software))
    for n in range(len(amplifiers) - 1):
        amplifiers[n].next_amplifier = amplifiers[n + 1]
    amplifiers[-1].next_amplifier = amplifiers[0]

    outputs = []
    for phase_setting_sequence in get_all_arrangements(phase_settings):
        for i in range(len(phase_setting_sequence)):
            amplifiers[i].reset()
            amplifiers[i].add_input(phase_setting_sequence[i])
        
        amplifiers[0].add_input(0)
        while not amplifiers[-1].finished:
            for amplifier in amplifiers:
                amplifier.amplify_till_halt()
        
        outputs.append(amplifiers[-1].last_output)

    print('Max thruster signal:', max(outputs))


def get_all_arrangements(items):
    if len(items) == 1:
        yield [items[0]]
    for i in range(len(items)):
        for arrangement in get_all_arrangements(items[:i] + items[i+1:]):
            yield [items[i], *arrangement]


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
