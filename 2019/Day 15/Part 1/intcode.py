from queue import Queue


class IntCode:
    PARAMETER_COUNTS = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 0}

    class ParameterModes:
        POSITION_MODE = 0
        IMMEDIATE_MODE = 1
        RELATIVE_MODE = 2

    def __init__(self, raw_int_code):
        self._int_code = [int(x) for x in raw_int_code.split(',')]
        self._input_buffer = Queue()
        self.output_buffer = Queue()
        self._i_ptr = 0
        self._relative_base = 0
        self.finished = False

    def execute_till_halt(self):
        while self._i_ptr < len(self._int_code):
            opcode, parameter_modes = self._get_instruction(self._i_ptr)
            parameter_count = IntCode.PARAMETER_COUNTS[opcode]
            parameter_modes = parameter_modes + [0]*(parameter_count - len(parameter_modes))
            parameters = self._get_parameters(self._i_ptr + 1, parameter_count)

            for j in range(len(parameters)):
                if parameter_modes[j] == IntCode.ParameterModes.IMMEDIATE_MODE:
                    parameters[j] = self._i_ptr + j + 1
                elif parameter_modes[j] == IntCode.ParameterModes.RELATIVE_MODE:
                    parameters[j] += self._relative_base
                
                # Check if location is outside memory, adjust memory capacity if necessary
                if parameters[j] >= len(self._int_code):
                    self._int_code += [0]*(parameters[j] + 1 - len(self._int_code))

            if opcode == 1:
                self._int_code[parameters[2]] = self._int_code[parameters[0]] + self._int_code[parameters[1]]
            elif opcode == 2:
                self._int_code[parameters[2]] = self._int_code[parameters[0]] * self._int_code[parameters[1]]
            elif opcode == 3:
                if self._is_input_available():
                    self._int_code[parameters[0]] = self._get_input()
                else:
                    return
            elif opcode == 4:
                self.output_buffer.put(self._int_code[parameters[0]])
            elif opcode == 5:
                if self._int_code[parameters[0]] != 0:
                    self._i_ptr = self._int_code[parameters[1]]
                    continue
            elif opcode == 6:
                if self._int_code[parameters[0]] == 0:
                    self._i_ptr = self._int_code[parameters[1]]
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
            elif opcode == 9:
                self._relative_base += self._int_code[parameters[0]]
            elif opcode == 99:
                self.finished = True
                return

            self._i_ptr += parameter_count + 1
    
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