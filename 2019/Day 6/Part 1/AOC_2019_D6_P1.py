# Advent Of Code 2019, Day 6, Part 1
# Author: Joth (https://github.com/joth00)

from os import path


def main():
    text_input = get_raw_input()
    raw_orbits = text_input.splitlines()
    orbits = [x.split(')') for x in raw_orbits]
    
    space_objects = dict()

    # Add all different space objects
    for orbit in orbits:
        if orbit[0] not in space_objects.keys():
            if orbit[0] == 'COM':
                space_objects['COM'] = Com()
            else:
                space_objects[orbit[0]] = SpaceObject(orbit[0])
        if orbit[1] not in space_objects.keys():
            space_objects[orbit[1]] = SpaceObject(orbit[1])
    
    # Set parent for every space object
    for orbit in orbits:
        space_objects[orbit[1]].set_parent(space_objects[orbit[0]])

    total_indirect_orbits = 0
    # Find number of indirect orbits for every space objects, add to sum
    for id_ in space_objects.keys():
        if isinstance(space_objects[id_], Com):
            continue
        total_indirect_orbits += space_objects[id_].get_indirect_orbits_count()
    
    print(total_indirect_orbits)

class SpaceObject:
    def __init__(self, id_):
        self.id = id_
        self.parent = None
    
    def set_parent(self, parent):
        self.parent = parent

    def get_indirect_orbits_count(self):
        return self.parent.get_parent_orbits_count()
   
    def get_parent_orbits_count(self):
        return self.parent.get_parent_orbits_count() + 1


class Com(SpaceObject):
    def __init__(self):
        super().__init__('COM')

    def get_parent_orbits_count(self):
        return 1

def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
