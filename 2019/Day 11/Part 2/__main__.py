# Advent of Code 2019, Day 11, Part 2

from os import path
from intcode import IntCode


class Color:
    BLACK = 0
    WHITE = 1


class ExtensibleColorGrid:
    def __init__(self, default_color, start_color):
        self._grid = {(0, 0): start_color}
        self._default_color = default_color

    def get_number_of_painted_panels(self):
        return len(self._grid.keys())

    def get_color_at(self, x, y):
        if not self._contains_location(x, y):
            return self._default_color
        return self._grid[(x, y)]
    
    def paint_color_at(self, x, y, color):
        self._grid[(x, y)] = color

    def _contains_location(self, x, y):
        return (x, y) in self._grid.keys()

    def visualize(self):
        min_x = min(self._grid, key=lambda c: c[0])[0]
        max_x = max(self._grid, key=lambda c: c[0])[0]
        min_y = min(self._grid, key=lambda c: c[1])[1]
        max_y = max(self._grid, key=lambda c: c[1])[1]

        for y in range(max_y, min_y - 1, -1):
            line = ''
            for x in range(min_x, max_x + 1):
                if self._contains_location(x, y):
                    if self._grid[(x, y)] == Color.WHITE:
                        line += '\u001b[37m\u2588\u001b[0m'*2
                    elif self._grid[(x, y)] == Color.BLACK:
                        line += '\u001b[30m\u2588\u001b[0m'*2
                else:
                    line += ' '*2
            print(line)


class Robot:
    def __init__(self, x, y, int_code_brain):
        self.brain = int_code_brain
        self.location = [x, y]
        self.rotation = 0

    def move(self, n):
        if self.rotation == 0:   self.location[1] += n
        elif self.rotation == 1: self.location[0] += n
        elif self.rotation == 2: self.location[1] -= n
        elif self.rotation == 3: self.location[0] -= n
    
    def rotate_right(self):
        self.rotation += 1
        self.rotation %= 4
    
    def rotate_left(self):
        self.rotation += 3
        self.rotation %= 4


def main():
    text_input = get_raw_input()
    grid = ExtensibleColorGrid(Color.BLACK, Color.WHITE)
    robot = Robot(0, 0, IntCode(text_input))

    while not robot.brain.finished:
        robot.brain.add_input(grid.get_color_at(*robot.location))

        robot.brain.execute_till_halt()

        color = robot.brain.output_buffer.get_nowait()
        rotation_direction = robot.brain.output_buffer.get_nowait()
        
        grid.paint_color_at(*robot.location, color)
    
        if rotation_direction == 0:
            robot.rotate_left()
        else:
            robot.rotate_right()

        robot.move(1)
    
    grid.visualize()


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


if __name__ == '__main__':
    main()