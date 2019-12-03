# Advent Of Code 2019, Day 3, Part 1
# Author: Joth (https://github.com/joth00)

from os import path


def main():
    text_input = get_raw_input()
    wire1, wire2 = text_input.splitlines()

    path1 = Path(wire1)
    path2 = Path(wire2)

    intersections = path1.get_intersections_with(path2)
    
    closest_intersection = min(intersections, key=lambda x: x.get_manhattan_distance_from_origin())
    smallest_distance = closest_intersection.get_manhattan_distance_from_origin()

    print('closest_intersection:', closest_intersection)
    print('with lowest distance:', smallest_distance)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_copy(self):
        return Point(self.x, self.y)
    
    def get_manhattan_distance_from(self, point):
        return abs(self.x - point.x) + abs(self.y - point.y)

    def get_manhattan_distance_from_origin(self):
        return abs(self.x) + abs(self.y)
    
    def move_right_by(self, value):
        self.x += value

    def move_left_by(self, value):
        self.x -= value

    def move_up_by(self, value):
        self.y += value

    def move_down_by(self, value):
        self.y -= value
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return str(self)


class Path:
    INSTRUCTION_TYPE_RIGHT = 'R'
    INSTRUCTION_TYPE_LEFT = 'L'
    INSTRUCTION_TYPE_UP = 'U'
    INSTRUCTION_TYPE_DOWN = 'D'

    def __init__(self, text_path):
        self.raw_path = text_path.split(',')
        self.path = self.get_connection_points_from_raw_path(self.raw_path)
    
    def get_connection_points_from_raw_path(self, raw_path):
        path = []
        
        tracker_position = Point(0, 0)
        path.append(tracker_position)
        
        for instruction in raw_path:
            instruction_type = instruction[0]
            instruction_value = int(instruction[1:])

            if instruction_type == Path.INSTRUCTION_TYPE_RIGHT:
                tracker_position.move_right_by(instruction_value)
            elif instruction_type == Path.INSTRUCTION_TYPE_LEFT:
                tracker_position.move_left_by(instruction_value)
            elif instruction_type == Path.INSTRUCTION_TYPE_UP:
                tracker_position.move_up_by(instruction_value)
            elif instruction_type == Path.INSTRUCTION_TYPE_DOWN:
                tracker_position.move_down_by(instruction_value)
            else:
                print('invalid instruction type')
                return

            path.append(tracker_position.get_copy())
        
        return path

    def get_intersections_with(self, other):
        intersections = []

        for i in range(1, len(self.path)):
            for j in range(1, len(other.path)):
                line_segment = (self.path[i - 1], self.path[i])
                other_line_segment = (other.path[j - 1], other.path[j])
                intersection = Path.get_line_segments_intersection(line_segment, other_line_segment)
                if intersection is not None:
                    intersections.append(intersection)
        
        return intersections

    
    @staticmethod
    def get_line_segments_intersection(line1, line2):
        if (Path.is_line_segment_horizontal(line1) and Path.is_line_segment_vertical(line2)):
            if Path.intersects(line1, line2):
                intersection = Point(line2[0].x, line1[0].y)
                return intersection
        elif (Path.is_line_segment_vertical(line1) and Path.is_line_segment_horizontal(line2)):
            if Path.intersects(line2, line1):
                intersection = Point(line1[0].x, line2[0].y)
                return intersection
        return None

    @staticmethod
    def is_line_segment_horizontal(line):
        return line[0].y == line[1].y
    
    @staticmethod
    def is_line_segment_vertical(line):
        return line[0].x == line[1].x
    
    @staticmethod
    def intersects(horizontal_line, vertical_line):
        y_constant = horizontal_line[0].y
        x_constant = vertical_line[0].x
        return ((vertical_line[0].y <= y_constant <= vertical_line[1].y
                    or vertical_line[1].y <= y_constant <= vertical_line[0].y)
                and (horizontal_line[0].x <= x_constant <= horizontal_line[1].x
                    or horizontal_line[1].x <= x_constant <= horizontal_line[0].x))


def get_raw_input():
    return open(get_input_file_path(), 'r').read()


def get_input_file_path():
    return path.join(path.dirname(__file__), 'input_clean.txt')


main()
