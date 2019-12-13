# Advent of Code 2019, Day 11, Part 1

from os import path
from intcode import IntCode


class Color:
    BLACK = 0
    WHITE = 1


class ExtensibleColorGrid:
    def __init__(self, default_color):
        self._grid = {(0, 0): default_color}
        self._default_color = default_color

    def get_number_of_painted_panels(self):
        return len(self._grid.keys())
    
    def get_color_at(self, x, y):
        if not self._contains_location(x, y):
            return self._default_color
        return self._grid[(x, y)]
    
    def paint_color_at(self, x, y, color):
        if not self._contains_location(x, y):
            self._add_location(x, y)
        self._grid[(x, y)] = color

    def _contains_location(self, x, y):
        return (x, y) in self._grid.keys()

    def _add_location(self, x, y):
        self._grid[(x, y)] = self._default_color


class Robot:
    ROTATIONS = ['up', 'right', 'down', 'left']

    def __init__(self, x, y, int_code_brain):
        self.brain = int_code_brain
        self.location = [x, y]
        self.rotation = 0

    def move(self, n):
        if self.rotation == 0:
            self.location[1] += n
        elif self.rotation == 1:
            self.location[0] += n
        elif self.rotation == 2:
            self.location[1] -= n
        elif self.rotation == 3:
            self.location[0] -= n
    
    def rotate_right(self):
        self.rotation += 1
        self.rotation %= len(Robot.ROTATIONS)
    
    def rotate_left(self):
        self.rotation += len(Robot.ROTATIONS) - 1
        self.rotation %= len(Robot.ROTATIONS)


def main():
    text_input = get_raw_input()
    grid = ExtensibleColorGrid(Color.BLACK)
    robot = Robot(0, 0, IntCode(text_input))

    while not robot.brain.finished:
        robot.brain.add_input(grid.get_color_at(*robot.location))
        robot.brain.execute_till_halt()
        grid.paint_color_at(*robot.location, robot.brain.output_buffer.get_nowait())
        if robot.brain.output_buffer.get_nowait() == 0:
            robot.rotate_left()
        else:
            robot.rotate_right()
        robot.move(1)
    
    print('Number of painted panels:', grid.get_number_of_painted_panels())



def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


if __name__ == '__main__':
    main()