# Advent of Code 2019, Day 5, Part 1
# Author: Joth (https://github.com/joth00)

from os import path


def main():
    text_input = get_raw_input()
    int_code = IntCode(text_input)

    int_code.execute()


class IntCode:
    INSTRUCTIONS = {
        1: (3, lambda int_code, loc_val1, loc_val2, loc: int_code.store(int_code.get(loc_val1) + int_code.get(loc_val2), loc)),
        2: (3, lambda int_code, loc_val1, loc_val2, loc: int_code.store(int_code.get(loc_val1) * int_code.get(loc_val2), loc)),
        3: (1, lambda int_code, loc: int_code.store(int(input('INPUT: ')), loc)),
        4: (1, lambda int_code, loc: print('OUTPUT:', int_code.get(loc))),
        99: (0, lambda int_code: int_code.finish_execution())
    }

    PARAMETER_MODES = {
        0: 'position mode',
        1: 'immediate mode'
    }

    def __init__(self, raw_int_code):
        self._int_code = list(int(x) for x in raw_int_code.split(','))
        self._finished_execution = False
    
    def get(self, location):
        return self._int_code[location]
    
    def store(self, value, location):
        self._int_code[location] = value
    
    def get_parameters(self, location, number_of_parameters):
        return self._int_code[location:location + number_of_parameters]
    
    def get_instruction(self, opcode_location):
        full_opcode = self.get(opcode_location)
        opcode = int(str(full_opcode)[-2:])
        parameter_modes = [int(x) for x in str(full_opcode)[:-2][::-1]]
        return (opcode, parameter_modes)
    
    def finish_execution(self):
        self._finished_execution = True

    def execute(self):
        i = 0
        while i < len(self._int_code):
            opcode, parameter_modes = self.get_instruction(i)

            if opcode not in IntCode.INSTRUCTIONS.keys():
                i += 1
                continue

            number_of_parameters = IntCode.INSTRUCTIONS[opcode][0]

            parameter_modes = parameter_modes + [0]*(number_of_parameters - len(parameter_modes))
            parameters = self.get_parameters(i + 1, number_of_parameters)

            for j in range(len(parameters)):
                parameter_mode = IntCode.PARAMETER_MODES[parameter_modes[j]]
                if parameter_mode == 'immediate mode':
                    parameters[j] = i + j + 1

            IntCode.INSTRUCTIONS[opcode][1](self, *parameters)

            if self._finished_execution:
                break

            i += number_of_parameters + 1


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


main()
