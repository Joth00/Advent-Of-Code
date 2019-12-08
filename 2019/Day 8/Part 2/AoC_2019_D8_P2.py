# Advent of Code 2019, Day 8, Part 2
# Author: Joth (https://github.com/joth00)

from os import path


def main():
    text_input = get_raw_input()
    raw_image = [int(x) for x in text_input]

    WIDTH = 25
    HEIGHT = 6

    layers = []

    i = 0
    while i < len(raw_image):
        j = i + WIDTH*HEIGHT
        layers.append(Layer.from_raw_data(raw_image[i:j], WIDTH, HEIGHT))
        i = j

    final_image = Image(WIDTH, HEIGHT)

    for layer in reversed(layers):
        layer.add_to_image(final_image)

    final_image.visualize()



class Image:
    BLACK = 0
    WHITE = 1
    TRANSPARENT = 2
    
    def __init__(self, width, height):
        self._data = [[0]*width for _ in range(height)]
    
    def put(self, pixel, row, column):
        if pixel != Image.TRANSPARENT:
            self._data[row][column] = pixel
    
    def visualize(self):
        for row in self._data:
            line = ''
            for pixel in row:
                if pixel == Image.BLACK:
                    line += '\u001b[30m\u2588'*2
                elif pixel == Image.WHITE:
                    line += '\u001b[37m\u2588'*2
                elif pixel == Image.TRANSPARENT:
                    line += ' '*2
            print(line)
        print('\u001b[0m')


class Layer:
    def __init__(self, layer_data):
        self._data = layer_data

    @staticmethod
    def from_raw_data(raw_data, width, height):
        data = [[0]*width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                data[i][j] = raw_data[i*width + j]
        return Layer(data)


    def add_to_image(self, img):
        for i in range(len(self._data)):
            for j in range(len(self._data[i])):
                img.put(self._data[i][j], i, j)


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
