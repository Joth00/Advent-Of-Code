# Advent Of Code 2019, Day 6, Part 2
# Author: Joth (https://github.com/joth00)

from os import path


def main():
    text_input = get_raw_input()
    orbits = [x.split(')') for x in text_input.splitlines()]
    space_objects = dict()

    # Add all different space objects
    for orbit in orbits:
        if orbit[0] not in space_objects.keys():
            space_objects[orbit[0]] = Com() if orbit[0] == 'COM' else SpaceObject()
        if orbit[1] not in space_objects.keys():
            space_objects[orbit[1]] = SpaceObject()
    
    # Set parent for every space object
    for orbit in orbits:
        space_objects[orbit[1]].set_parent(space_objects[orbit[0]])

    parents_you = space_objects['YOU'].get_parents()
    parents_santa = space_objects['SAN'].get_parents()

    for parent_you in parents_you:
        for parent_santa in parents_santa:
            if parent_you == parent_santa:
                orbital_transfer_count = parents_you.index(parent_you) + parents_santa.index(parent_santa)
                print('Minimal number of orbital transfers required:', orbital_transfer_count)
                return


class SpaceObject:
    def __init__(self):
        self.parent = None
    
    def set_parent(self, parent):
        self.parent = parent
   
    def get_parents(self):
        return [self.parent, *self.parent.get_parents()]


class Com(SpaceObject):
    def __init__(self):
        super().__init__()

    def get_parents(self):
        return [self]


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
