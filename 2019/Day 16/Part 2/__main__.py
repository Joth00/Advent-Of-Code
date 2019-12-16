# Advent of Code 2019, Day 16, Part 1

from os import path, system
from math import ceil


def main():
    text_input = get_raw_input()
    message_offset = int(text_input[:7])
    assert message_offset >= len(text_input)/2
    input_signal = list(int(x) for x in text_input)
    input_signal = (input_signal*10000)[message_offset:]
    signal_length = len(input_signal)
    
    phase = 1
    while phase <= 100:
        for i in range(signal_length-2, -1, -1):
            input_signal[i] = (input_signal[i] + input_signal[i + 1]) % 10
        phase += 1

    eight_digit_message = ''.join(str(x) for x in input_signal[:8])

    print('Eight-digit message after 100 phases of FFT:', eight_digit_message)


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


if __name__ == '__main__':
    main()