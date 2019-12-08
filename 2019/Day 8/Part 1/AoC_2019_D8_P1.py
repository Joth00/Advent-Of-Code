# Advent of Code 2019, Day 8, Part 1
# Author: Joth (https://github.com/joth00)

from os import path


def main():
    text_input = get_raw_input()
    raw_image = text_input

    WIDTH = 25
    HEIGHT = 6

    layers = []

    i = 0
    while i < len(raw_image):
        j = i + WIDTH*HEIGHT
        layers.append(raw_image[i:j])
        i = j

    layer_wiht_fewest_0_digits = min(layers, key=lambda x: x.count('0'))
    result = layer_wiht_fewest_0_digits.count('1') * layer_wiht_fewest_0_digits.count('2')

    print('Result:', result)


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
