# Advent of Code 2019, Day 13, Part 2

import os
from intcode import IntCode


class Tiles:
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


class Joystick:
    LEFT = -1
    NEUTRAL = 0
    RIGHT = 1


class Directions:
    LEFT = 0
    UNDEFINED = 1
    RIGHT = 2


class Ball:
    def __init__(self, x_pos=0):
        self.x = x_pos
        self.old_x = x_pos
        self.direction = Directions.UNDEFINED

    def set_x_pos(self, x):
        self.old_x = self.x
        self.x = x
    
    def update_direction(self):
        if self.old_x < self.x:
            self.direction = Directions.RIGHT
        elif self.old_x > self.x:
            self.direction = Directions.LEFT
        else:
            self.direction = Directions.UNDEFINED


class Paddle:
    def __init__(self, x_pos=0):
        self.x = x_pos


def main():
    text_input = get_raw_input()
    int_code = IntCode(text_input)

    int_code._int_code[0] = 2
    
    tiles = dict()

    score = 0
    paddle = Paddle()
    ball = Ball()
    while not int_code.finished:
        for co in tiles.keys():
            if tiles[co] == Tiles.PADDLE:
                paddle.x = co[0]
            elif tiles[co] == Tiles.BALL:
                ball.set_x_pos(co[0])

        ball.update_direction()

        if ball.direction == Directions.LEFT and paddle.x > ball.x:
            int_code.add_input(Joystick.LEFT)
        elif ball.direction == Directions.RIGHT and ball.x > paddle.x:
            int_code.add_input(Joystick.RIGHT)
        elif paddle.x > ball.x:
            int_code.add_input(Joystick.LEFT)
        elif paddle.x < ball.x:
            int_code.add_input(Joystick.RIGHT)
        else:
            int_code.add_input(Joystick.NEUTRAL)

        int_code.execute_till_halt()

        output_instructions = list(int_code.output_buffer.queue)

        i = 0
        while i + 2 < len(output_instructions):
            x, y, id_ = output_instructions[i:i+3]
            if x == -1 and y == 0:
                score = id_
            else:
                tiles[(x, y)] = id_
            i += 3

        print_tiles(tiles)

    print('Score after all blocks are broken:', score)


def print_tiles(tiles):
    os.system('clear')
    min_x = min(tiles.keys(), key=lambda c: c[0])[0]
    max_x = max(tiles.keys(), key=lambda c: c[0])[0]
    min_y = min(tiles.keys(), key=lambda c: c[1])[1]
    max_y = max(tiles.keys(), key=lambda c: c[1])[1]
    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x, max_x + 1):
            if (x, y) in tiles.keys():
                tile = tiles[(x, y)]
                if tile == Tiles.EMPTY:
                    line += '  '
                elif tile == Tiles.WALL:
                    line += u'\u2588'*2
                elif tile == Tiles.BLOCK:
                    line += u'\u001b[32m\u228f\u2290\u001b[0m' # '\u001b[32m\u2588\u001b[0m'*2
                elif tile == Tiles.PADDLE:
                    line += u'\u001b[34m\u2acd\u2ace\u001b[0m'
                elif tile == Tiles.BALL:
                    line += u'\u001b[31m\u2b24 \u001b[0m'
            else:
                line += '  '
        print(line)


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return os.path.join(os.path.dirname(__file__), 'input.txt')


if __name__ == '__main__':
    main()