# Advent of Code 2019, Day 16, Part 1

from os import path, system
from math import ceil


def main():
    text_input = get_raw_input()
    input_signal = list(int(e) for e in text_input)
    signal_length = len(input_signal)
    
    phase = 1
    while phase <= 100:
        output_signal = [0]*len(input_signal)
        for i in range(signal_length):
            output_element = 0
            repition_factor = i + 1
            j = repition_factor - 1     # skip the first element of the pattern
            while j < signal_length:
                output_element += sum(input_signal[j:j+repition_factor])
                j += 2*repition_factor
                output_element -= sum(input_signal[j:j+repition_factor])
                j += 2*repition_factor
            output_signal[i] = abs(output_element) % 10
        input_signal = output_signal[:]
        phase += 1

    first_eight_digits = ''.join(str(x) for x in input_signal[:8])

    print('First eight digits in the final output list after 100 phases of FFT:', first_eight_digits)


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


if __name__ == '__main__':
    main()