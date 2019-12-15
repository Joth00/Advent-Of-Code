# Advent of Code 2019, Day 15, Part 1

from os import path, system
from intcode import IntCode


class Directions:
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

    @staticmethod
    def opposite(direction):
        if direction == Directions.NORTH:
            return Directions.SOUTH
        elif direction == Directions.EAST:
            return Directions.WEST
        elif direction == Directions.SOUTH:
            return Directions.NORTH
        elif direction == Directions.WEST:
            return Directions.EAST
        else:
            return None


class StatusCodes:
    HIT_WALL = 0
    MOVED_OK = 1
    MOVED_FINISHED = 2


class LocationTypes:
    EMPTY = 0
    WALL = 1
    OXYGEN_SYSTEM = 2


class RepairDroid:
    def __init__(self, x, y, direction, raw_int_code_software):
        self._x = x
        self._y = y
        self.direction = direction
        self._brain = IntCode(raw_int_code_software) if raw_int_code_software is not None else None
        self.travelled_distance = 0

    def get_location(self):
        return (self._x, self._y)
    
    def execute(self):
        self._brain.add_input(self.direction)
        self._brain.execute_till_halt()
    
    def get_reply(self):
        return self._brain.output_buffer.get_nowait()
    
    def move(self,):
        if self.direction == Directions.NORTH:
            self._y += 1
        elif self.direction == Directions.EAST:
            self._x += 1
        elif self.direction == Directions.SOUTH:
            self._y -= 1
        elif self.direction == Directions.WEST:
            self._x -= 1
        self.travelled_distance += 1

    @staticmethod
    def from_repair_droid(base_repair_droid):
        new_repair_droid = RepairDroid(*base_repair_droid.get_location(), base_repair_droid.direction, None)
        new_repair_droid.travelled_distance = base_repair_droid.travelled_distance
        new_repair_droid._brain = IntCode('0')
        new_repair_droid._brain._int_code = base_repair_droid._brain._int_code[:]
        new_repair_droid._brain._input_buffer = base_repair_droid._brain._input_buffer
        new_repair_droid._brain.output_buffer = base_repair_droid._brain.output_buffer
        new_repair_droid._brain._i_ptr = base_repair_droid._brain._i_ptr
        new_repair_droid._brain._relative_base = base_repair_droid._brain._relative_base
        new_repair_droid._brain.finished = base_repair_droid._brain.finished
        return new_repair_droid


def main():
    text_input = get_raw_input()
    origin = (0, 0)
    repair_droids = [RepairDroid(*origin, None, text_input)]
    area = {origin: LocationTypes.EMPTY}

    repair_droid_at_oxygen_system = None

    finished = False
    while not finished:
        new_repair_droids = []
        for base_repair_droid in repair_droids:
            directions = get_possible_directions(base_repair_droid.get_location(), Directions.opposite(base_repair_droid.direction), area)
            for direction in directions:
                repair_droid = RepairDroid.from_repair_droid(base_repair_droid)
                repair_droid.direction = direction
                repair_droid.execute()
                status = repair_droid.get_reply()
                repair_droid.move()
                if status == StatusCodes.HIT_WALL:
                    area[repair_droid.get_location()] = LocationTypes.WALL
                elif status == StatusCodes.MOVED_OK:
                    area[repair_droid.get_location()] = LocationTypes.EMPTY
                    new_repair_droids.append(repair_droid)
                elif status == StatusCodes.MOVED_FINISHED:
                    area[repair_droid.get_location()] = LocationTypes.OXYGEN_SYSTEM
                    new_repair_droids.append(repair_droid)
                    repair_droid_at_oxygen_system = repair_droid
                    finished = True
                    break
            if finished:
                break
        repair_droids = new_repair_droids[:]
        # print_area(area, repair_droids)
    
    # print_area(area)
    
    closest_distance_to_origin = repair_droid_at_oxygen_system.travelled_distance

    print('Fewest number of movement commands:', closest_distance_to_origin)


def get_possible_directions(base_location, direction_to_avoid, area):
    x, y = base_location

    locations = [
        ((x, y + 1), Directions.NORTH),
        ((x + 1, y), Directions.EAST),
        ((x, y - 1), Directions.SOUTH),
        ((x - 1, y), Directions.WEST)
    ]

    for location in locations:
        if (location[0] not in area or area[location[0]] == LocationTypes.EMPTY) and direction_to_avoid != location[1]:
            yield location[1]


def print_area(area, droids=None):
    system('clear')
    locations = list(area.keys())
    if droids is not None:
        for droid in droids:
            locations.append(droid.get_location())

    x_min = min(locations, key=lambda c: c[0])[0]
    x_max = max(locations, key=lambda c: c[0])[0]
    y_min = min(locations, key=lambda c: c[1])[1]
    y_max = max(locations, key=lambda c: c[1])[1]

    for y in range(y_max, y_min - 1, -1):
        line = ''
        for x in range(x_min, x_max + 1):
            if droids is not None and (x, y) in [d.get_location() for d in droids]:
                droid = list(d for d in droids if d.get_location() == (x, y))[0]
                line += '\u001b[34m'
                if droid.direction == Directions.NORTH:
                    line += '\u02c4'
                elif droid.direction == Directions.EAST:
                    line += '\u02c3'
                elif droid.direction == Directions.SOUTH:
                    line += '\u02c5'
                elif droid.direction == Directions.WEST:
                    line += '\u02c2'
                line += '\u001b[0m'
            elif (x, y) == (0, 0):
                line += '\u001b[32m\u25c9\u001b[0m'
            elif (x, y) not in area.keys():
                line += ' '
            elif area[(x, y)] == LocationTypes.EMPTY:
                line += ' '
            elif area[(x, y)] == LocationTypes.WALL:
                line += '\u2588'
            elif area[(x, y)] == LocationTypes.OXYGEN_SYSTEM:
                line += '\u001b[31;1m\u2588\u001b[0m'
        print(line)


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


if __name__ == '__main__':
    main()