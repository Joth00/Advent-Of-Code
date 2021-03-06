# Advent of Code 2019, Day 7, Part 1

from os import path
from amplifier import Amplifier


def main():
    text_input = get_raw_input()
    amplifier_controller_software = [int(x) for x in text_input.split(',')]
    phase_settings = [0, 1, 2, 3, 4]

    amplifiers = []
    for _ in range(len(phase_settings)):
        amplifiers.append(Amplifier(amplifier_controller_software))

    outputs = []
    for phase_setting_sequence in get_all_arrangements(phase_settings):
        output = 0
        for i in phase_setting_sequence:
            amplifier = amplifiers[i]
            amplifier.add_input(phase_setting_sequence[i])
            amplifier.add_input(output)
            amplifier.execute()
            output = amplifier.outputs[0]
            amplifier.reset()
        outputs.append(output)

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


if __name__ == '__main__':
    main()