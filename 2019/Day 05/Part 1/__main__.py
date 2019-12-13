# Advent of Code 2019, Day 5, Part 1

from os import path
from queue import Queue


def main():
    text_input = get_raw_input()
    int_code = IntCode(text_input)

    int_code.add_input(1)
    int_code.execute()


class NotEnoughInputsError(Exception):
    """ Raised when not enough inputs given. """
    pass


class IntCode:
    PARAMETER_COUNTS = {1: 3, 2: 3, 3: 1, 4: 1, 99: 0}

    class ParameterModes:
        POSITION_MODE = 0
        IMMEDIATE_MODE = 1

    def __init__(self, raw_int_code):
        self._int_code = list(int(x) for x in raw_int_code.split(','))
        self._input_buffer = Queue()

    def execute(self):
        i = 0   # Instruction pointer
        while i < len(self._int_code):
            opcode, parameter_modes = self._get_instruction(i)
            parameter_count = IntCode.PARAMETER_COUNTS[opcode]
            parameter_modes = parameter_modes + [0]*(parameter_count - len(parameter_modes))
            parameters = self._get_parameters(i + 1, parameter_count)

            for j in range(len(parameters)):
                if parameter_modes[j] == IntCode.ParameterModes.IMMEDIATE_MODE:
                    parameters[j] = i + j + 1

            if opcode == 1:
                self._int_code[parameters[2]] = self._int_code[parameters[0]] + self._int_code[parameters[1]]
            elif opcode == 2:
                self._int_code[parameters[2]] = self._int_code[parameters[0]] * self._int_code[parameters[1]]
            elif opcode == 3:
                if self._is_input_available():
                    self._int_code[parameters[0]] = self._get_input()
                else:
                    raise NotEnoughInputsError
            elif opcode == 4:
                print('OUTPUT:', self._int_code[parameters[0]])
            elif opcode == 99:
                break
 
            i += parameter_count + 1
    
    def _get_instruction(self, opcode_location):
        full_opcode = self._int_code[opcode_location]
        opcode = full_opcode % 100
        parameter_modes = [int(x) for x in str(full_opcode)[:-2][::-1]]
        return (opcode, parameter_modes)
    
    def _get_parameters(self, location, parameter_count):
        return self._int_code[location:location + parameter_count]
    
    def _is_input_available(self):
        return not self._input_buffer.empty()

    def _get_input(self):
        return self._input_buffer.get_nowait()
    
    def add_input(self, input_):
        self._input_buffer.put(input_)


def get_raw_input():
    return open(retrieve_input_file_path(), 'r').read()


def retrieve_input_file_path():
    return path.join(path.dirname(__file__), 'input.txt')


if __name__ == '__main__':
    main()