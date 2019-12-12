from queue import Queue


class NotEnoughInputsError(Exception):
    """ Raised when not enough inputs given. """
    pass


class Amplifier:
    PARAMETER_COUNTS = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0}

    class ParameterModes:
        POSITION_MODE = 0
        IMMEDIATE_MODE = 1

    def __init__(self, int_code):
        self._original_int_code = int_code[:]
        self._int_code = int_code[:]
        self._input_buffer = Queue()
        self.outputs = []
    
    def reset(self):
        self._int_code = self._original_int_code[:]
        self._input_buffer.queue.clear()
        self.outputs = []

    def execute(self):
        i = 0   # Instruction pointer
        while i < len(self._int_code):
            opcode, parameter_modes = self._get_instruction(i)
            parameter_count = Amplifier.PARAMETER_COUNTS[opcode]
            parameter_modes = parameter_modes + [0]*(parameter_count - len(parameter_modes))
            parameters = self._get_parameters(i + 1, parameter_count)

            for j in range(len(parameters)):
                if parameter_modes[j] == Amplifier.ParameterModes.IMMEDIATE_MODE:
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
                self.outputs.append(self._int_code[parameters[0]])
            elif opcode == 5:
                if self._int_code[parameters[0]] != 0:
                    i = self._int_code[parameters[1]]
                    continue
            elif opcode == 6:
                if self._int_code[parameters[0]] == 0:
                    i = self._int_code[parameters[1]]
                    continue
            elif opcode == 7:
                if self._int_code[parameters[0]] < self._int_code[parameters[1]]:
                    self._int_code[parameters[2]] = 1
                else:
                    self._int_code[parameters[2]] = 0
            elif opcode == 8:
                if self._int_code[parameters[0]] == self._int_code[parameters[1]]:
                    self._int_code[parameters[2]] = 1
                else:
                    self._int_code[parameters[2]] = 0
            elif opcode == 99:
                break

            i += parameter_count + 1
    
    def _get_instruction(self, opcode_location):
        full_opcode = self._int_code[opcode_location]
        opcode = full_opcode % 100
        parameter_modes = [int(x) for x in str(full_opcode)[:-2][::-1]]
        return (opcode, parameter_modes)
    
    def _get_parameters(self, location, number_of_parameters):
        return self._int_code[location : location + number_of_parameters]
    
    def _is_input_available(self):
        return not self._input_buffer.empty()

    def _get_input(self):
        return self._input_buffer.get_nowait()
    
    def add_input(self, input_):
        self._input_buffer.put(input_)