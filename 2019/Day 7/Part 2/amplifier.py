from queue import Queue

class Amplifier:
    PARAMETER_COUNTS = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0}

    def __init__(self, int_code, next_amplifier=None):
        self._original_int_code = int_code
        self._int_code = int_code
        self._input_buffer = Queue()
        self.next_amplifier = next_amplifier
        self.finished = False
        self.last_output = None
        self._i_ptr = 0     # Instruction pointer
    
    def reset(self):
        self._int_code = self._original_int_code[:]
        self._input_buffer.queue.clear()
        self.finished = False
        self.last_output = None
        self._i_ptr = 0

    def amplify_till_halt(self):
        while self._i_ptr < len(self._int_code):
            opcode, parameter_modes = self._get_instruction(self._i_ptr)

            if opcode not in Amplifier.PARAMETER_COUNTS.keys():
                print('INVALID OPCODE')
                self._i_ptr += 1
                continue

            parameter_count = Amplifier.PARAMETER_COUNTS[opcode]

            parameter_modes = parameter_modes + [0]*(parameter_count - len(parameter_modes))
            parameters = self._get_parameters(self._i_ptr + 1, parameter_count)

            for j in range(len(parameters)):
                if parameter_modes[j] == 1:
                    # immediate mode, replace value by value index (location)
                    parameters[j] = self._i_ptr + j + 1

            if opcode == 1:
                self._int_code[parameters[2]] = self._int_code[parameters[0]] + self._int_code[parameters[1]]
            elif opcode == 2:
                self._int_code[parameters[2]] = self._int_code[parameters[0]] * self._int_code[parameters[1]]
            elif opcode == 3:
                if self._is_input_available():
                    self._int_code[parameters[0]] = self._get_input()
                else:
                    break
            elif opcode == 4:
                self._output(self._int_code[parameters[0]])
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
            elif opcode == 99:
                self.finished = True
                break

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

    def _output(self, output):
        self.last_output = output
        self.next_amplifier.add_input(output)
    
    def add_input(self, input_):
        self._input_buffer.put(input_)