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

    def get_manhattan_distance_from_origin(self):
        return abs(self.x) + abs(self.y)


class Path:
    def __init__(self, text_path):
        self.raw_path = text_path.split(',')
        self.path = self.get_connection_points_from_raw_path(self.raw_path)
    
    def get_connection_points_from_raw_path(self, raw_path):
        path = [Point(0, 0)]        
        tracker_position = Point(0, 0)

        for instruction in raw_path:
            instruction_type = instruction[0]
            instruction_value = int(instruction[1:])

            if instruction_type == 'R':
                tracker_position.x += instruction_value
            elif instruction_type == 'L':
                tracker_position.x -= instruction_value
            elif instruction_type == 'U':
                tracker_position.y += instruction_value
            elif instruction_type == 'D':
                tracker_position.y -= instruction_value

            path.append(Point(tracker_position.x, tracker_position.y))

        return path

    def get_intersections_with(self, other):
        intersections = []

        for i in range(1, len(self.path)):
            for j in range(1, len(other.path)):
                line_segment = (self.path[i - 1], self.path[i])
                other_line_segment = (other.path[j - 1], other.path[j])
                intersection = Path.get_intersection_of_line_segements(line_segment, other_line_segment)
                if intersection is not None:
                    intersections.append(intersection)
        
        return intersections

    
    @staticmethod
    def get_intersection_of_line_segements(line1, line2):
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
        horizontal_line = sorted(horizontal_line, key=lambda p: p.x)
        vertical_line = sorted(vertical_line, key=lambda p: p.y)
        return (vertical_line[0].y <= y_constant <= vertical_line[1].y
                and horizontal_line[0].x <= x_constant <= horizontal_line[1].x)


def get_raw_input():
    return open(get_input_file_path(), 'r').read()


def get_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
