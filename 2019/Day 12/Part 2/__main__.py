# Advent of Code 2019, Day 12, Part 2

from os import path
import re


class Moon:
    def __init__(self, position):
        self.position = position
        self.velocity = 0

    def apply_velocity(self):
        self.position += self.velocity

    @staticmethod
    def apply_gravity_between(moon1, moon2):
        if moon1.position != moon2.position:
            moon1.velocity += 1 if moon1.position < moon2.position else -1
            moon2.velocity -= 1 if moon1.position < moon2.position else -1


def main():
    text_input = get_raw_input()

    moons_data = []
    for raw_moon_data in text_input.splitlines():
        moons_data.append(extract_moon_data(raw_moon_data))

    pairs = get_all_unique_pairs(range(len(moons_data)))

    steps = []

    for dim in range(3):
        moons = list(Moon(moon_data[dim]) for moon_data in moons_data)
        start_positions = tuple(moon.position for moon in moons)
        start_velocities = tuple(moon.velocity for moon in moons)
        step = 0
        while True:
            for i, j in pairs:
                Moon.apply_gravity_between(moons[i], moons[j])

            for moon in moons:
                moon.apply_velocity()

            step += 1

            if (tuple(moon.position for moon in moons) == start_positions
                    and tuple(moon.velocity for moon in moons) == start_velocities):
                break
        
        steps.append(step)

    total_steps = lcm(steps)
    
    print('Steps it takes for the universe to repeat:', total_steps)


def get_all_unique_pairs(elements):
    pairs = set()
    for i in elements:
        for j in elements:
            if (j, i) not in pairs:
                pairs.add((i, j))
    return pairs


def extract_moon_data(raw_data):
    pattern = r'^<x=(?P<x>.*), y=(?P<y>.*), z=(?P<z>.*)>$'
    match = re.match(pattern, raw_data)
    x, y, z = match.group('x'), match.group('y'), match.group('z')
    return (int(x), int(y), int(z))


def lcm(items):
    if len(items) == 1:
        return items[0]
    a = items[0]
    b = lcm(items[1:])
    c = b
    while c % a != 0:
        c += b
    return c


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


if __name__ == '__main__':
    main()