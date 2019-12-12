# Advent of Code 2019, Day 3, Part 2
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
                        
                        if connection1[2] == 0:
                            steps1 = connection1[3] + (intersection[0] - connection1[0][0])
                        else:
                            steps1 = connection1[3] - (intersection[0] - connection1[0][0])
                        
                        if connection2[2] == 0:
                            steps2 = connection2[3] + (intersection[1] - connection2[0][1])
                        else:
                            steps2 = connection2[3] - (intersection[1] - connection2[0][1])

                        intersections.append((intersection, steps1, steps2))
            elif (connection1[0][0] == connection1[1][0]
                    and connection2[0][1] == connection2[1][1]):
                # connection1 is vertical, connection2 is horizontal
                if (connection2[0][1] <= connection1[1][1]
                        and connection2[0][1] >= connection1[0][1]
                        and connection1[0][0] >= connection2[0][0]
                        and connection1[0][0] <= connection2[1][0]):
                        # find intersection
                        intersection = (connection1[0][0], connection2[0][1])                
                        
                        if connection1[2] == 0:
                            steps1 = connection1[3] + (intersection[1] - connection1[0][1])
                        else:
                            steps1 = connection1[3] - (intersection[1] - connection1[0][1])

                        if connection2[2] == 0:
                            steps2 = connection2[3] + (intersection[0] - connection2[0][0])
                        else:
                            steps2 = connection2[3] - (intersection[0] - connection2[0][0])
                        
                        intersections.append((intersection, steps1, steps2))
    
    intersections = [x for x in intersections if x[0] != (0, 0)]

    best_intersection = min(intersections, key=lambda x: x[1] + x[2])
    least_steps = best_intersection[1] + best_intersection[2]
    
    print('best intersection:', best_intersection)
    print('with least steps:', least_steps)


def find_all_connections(commands):
    connections = []
    position = [0, 0]
    steps = 0
    for i, x in enumerate(commands):
        command = x[0]
        value = int(x[1:])
        if command == 'R':
            steps += value
            connections.append(((*position,), (position[0] + value, position[1]), 0, steps))
            position[0] += value
        elif command == 'L':
            steps += value
            connections.append(((position[0] - value, position[1]), (*position,), 1, steps))
            position[0] -= value
        elif command == 'U':
            steps += value
            connections.append(((*position,), (position[0], position[1] + value), 0, steps))
            position[1] += value
        elif command == 'D':
            steps += value
            connections.append(((position[0], position[1] - value), (*position,), 1, steps))
            position[1] -= value
    return connections


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
