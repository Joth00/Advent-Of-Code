# Advent of Code 2019, Day 10, Part 1
# Author: Joth (https://github.com/joth00)

from os import path

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'({self.x}, {self.y})'


class Asteroid:
    def __init__(self, location):
        self.location = location
        self.detectable_asteroid_count = 0

    def is_between(self, asteroid1, asteroid2):
        x, y = self.location.x, self.location.y
        x1, y1 = asteroid1.location.x, asteroid1.location.y
        x2, y2 = asteroid2.location.x, asteroid2.location.y

        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        if min_x <= x <= max_x and min_y <= y <= max_y:
            return y - y1 == ((y2 - y1)/(x2 - x1))*(x - x1) if x1 != x2 else x1 == x

        return False


class SpaceMap:

    class Symbols:
        EMPTY = '.'
        ASTEROID = '#'

    def __init__(self, raw_map):
        self._map = list(list(line) for line in raw_map.splitlines())
        self._HEIGHT = len(self._map)
        self._WIDTH = len(self._map[0])
        self._asteroids = []
        self._detect_asteroids()
        self._evaluate_every_asteroid()

    def _detect_asteroids(self):
        for y in range(self._HEIGHT):
            for x in range(self._WIDTH):
                location = Location(x, y)
                if self._get(location) == SpaceMap.Symbols.ASTEROID:
                    asteroid = Asteroid(location)
                    self._set(location, asteroid)
                    self._asteroids.append(asteroid)
                else:
                    self._set(location, None)

    def get_best_evaluated_asteroid(self):
        return max(self._asteroids, key=lambda x: x.detectable_asteroid_count)

    def _evaluate_every_asteroid(self):
        for asteroid in self._asteroids:
            self._determinate_detectable_asteroids_for(asteroid)

    def _determinate_detectable_asteroids_for(self, asteroid):
        asteroid.detectable_asteroid_count = 0
        for possible_detectable_asteroid in [x for x in self._asteroids if x != asteroid]:
            for possible_blocking_asteroid in [x for x in self._asteroids if x != possible_detectable_asteroid and x != asteroid]:
                if possible_blocking_asteroid.is_between(asteroid, possible_detectable_asteroid):
                    break
            else:
                asteroid.detectable_asteroid_count += 1

    def _is_asteroid(self, location):
        return isinstance(self._get(location), Asteroid)
    
    def _is_empty(self, location):
        return self._get(location) is None
    
    def _get(self, location):
        return self._map[location.y][location.x]

    def _set(self, location, value):
        self._map[location.y][location.x] = value


def main():
    text_input = get_raw_input()
    space_map = SpaceMap(text_input)
    best_asteroid = space_map.get_best_evaluated_asteroid()
    print('Best asteroid:', best_asteroid.location)
    print('Detectable asteroid count:', best_asteroid.detectable_asteroid_count)


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
