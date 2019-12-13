# Advent of Code 2019, Day 12, Part 1

from os import path
import re


class Moon:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]    # position
        self.vel = [0, 0, 0]    # velocity

    @staticmethod
    def from_raw_data(raw_text):
        pattern = r'^<x=(?P<x>.*), y=(?P<y>.*), z=(?P<z>.*)>$'
        match = re.match(pattern, raw_text)
        x, y, z = match.group('x'), match.group('y'), match.group('z')
        return Moon(int(x), int(y), int(z))

    @staticmethod
    def apply_gravity_between(moon1, moon2):
        for i in range(3):
            if moon1.pos[i] < moon2.pos[i]:
                moon1.vel[i] += 1
                moon2.vel[i] -= 1
            elif moon1.pos[i] > moon2.pos[i]:
                moon1.vel[i] -= 1
                moon2.vel[i] += 1
            else:
                pass

    def apply_velocity(self):
        for i in range(3):
            self.pos[i] += self.vel[i]

    def get_potential_energy(self):
        return sum(abs(val) for val in self.pos)

    def get_kinetic_energy(self):
        return sum(abs(val) for val in self.vel)

    def __repr__(self):
        return f'pos=<x={self.pos[0]}, y={self.pos[1]}, z={self.pos[2]}>,  vel=<x={self.vel[0]}, y={self.vel[1]}, z={self.vel[2]}>'


def main():
    text_input = get_raw_input()
    steps = 1000

    moons = []
    for raw_moon_data in text_input.splitlines():
        moons.append(Moon.from_raw_data(raw_moon_data))

    pairs = get_all_unique_pairs(range(len(moons)))

    for _ in range(steps):
        for i, j in pairs:
            Moon.apply_gravity_between(moons[i], moons[j])

        for moon in moons:
            moon.apply_velocity()

    energy_total = 0
    for moon in moons:
        energy_total += moon.get_potential_energy() * moon.get_kinetic_energy()
    
    print('Sum of total energy:', energy_total)


def get_all_unique_pairs(elements):
    pairs = set()
    for i in elements:
        for j in elements:
            if (j, i) not in pairs:
                pairs.add((i, j))
    return pairs


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


if __name__ == '__main__':
    main()