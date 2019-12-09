# Advent of Code 2019, Day 3, Part 1
# Author: Joth (https://github.com/joth00)

from os import path


def main():
    text_input = get_raw_input()
    wire1, wire2 = [x.split(',') for x in text_input.splitlines()]

    connections1 = find_all_connections(wire1)
    connections2 = find_all_connections(wire2)

    intersections = []

    for connection1 in connections1:
        for connection2 in connections2:
            if (connection1[0][1] == connection1[1][1]
                    and connection2[0][0] == connection2[1][0]):
                # connection1 is horizontal, connection2 is vertical
                if (connection1[0][1] <= connection2[1][1]
                        and connection1[0][1] >= connection2[0][1]
                        and connection2[0][0] >= connection1[0][0]
                        and connection2[0][0] <= connection1[1][0]):
                        # find intersection
                        intersection = (connection2[0][0], connection1[0][1])
                        intersections.append(intersection)
            elif (connection1[0][0] == connection1[1][0]
                    and connection2[0][1] == connection2[1][1]):
                # connection1 is vertical, connection2 is horizontal
                if (connection2[0][1] <= connection1[1][1]
                        and connection2[0][1] >= connection1[0][1]
                        and connection1[0][0] >= connection2[0][0]
                        and connection1[0][0] <= connection2[1][0]):
                        # find intersection
                        intersection = (connection1[0][0], connection2[0][1])                
                        intersections.append(intersection)
    
    if (0, 0) in intersections:
        intersections.remove((0, 0))

    closest_intersection = min(intersections, key=calculateManhattanDistanceFromOrigin)
    lowest_distance = get_manhattan_distance_from_origin(closest_intersection)
    
    print('closest_intersection:', closest_intersection)
    print('with lowest distance:', lowest_distance)


def find_all_connections(commands):
    connections = []
    position = [0, 0]
    for x in commands:
        command = x[0]
        value = int(x[1:])
        if command == 'R':
            connections.append(((*position,), (position[0] + value, position[1])))
            position[0] += value
        elif command == 'L':
            connections.append(((position[0] - value, position[1]), (*position,)))
            position[0] -= value
        elif command == 'U':
            connections.append(((*position,), (position[0], position[1] + value)))
            position[1] += value
        elif command == 'D':
            connections.append(((position[0], position[1] - value), (*position,)))
            position[1] -= value
    return connections


def get_manhattan_distance_from_origin(point):
    return abs(point[1]) + abs(point[0])


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
