from itertools import permutations
from pyhelper.pyimport import seperator_to_list
input_program = seperator_to_list('2019/input/day7_input.txt', seperator = ',', cast = int)

class amp:
    ptr = ptr_inputs = 0

    def __init__(self, program, starting_inputs):
        self.program = program
        self.inputs = starting_inputs

    def calc(self):
        vars_per_opcode = {1: 3, 2: 3, 3: 1, 4: 1, 99: 0, 5: 2, 6: 2, 7: 3, 8: 3}
        modes = str(self.program[self.ptr])[-3::-1]
        opcode = self.program[self.ptr] % 100
        stuffed_modes = ''.join([modes, '0' * (vars_per_opcode[opcode] - len(modes))])
        params = [self.program[self.program[self.ptr + i_var]] if var == '0' else self.program[self.ptr + i_var] for i_var, var in enumerate(stuffed_modes, start = 1)]
        ptr_initial = self.ptr
        out = status = None
        match opcode:
            case 1: self.program[self.program[self.ptr + 3]] = params[0] + params[1]
            case 2: self.program[self.program[self.ptr + 3]] = params[0] * params[1]
            case 3: 
                if self.ptr_inputs < len(self.inputs):
                    self.program[self.program[self.ptr+1]] = self.inputs[self.ptr_inputs]
                    self.ptr_inputs += 1
                else:
                    status = 3
            case 4: out = self.program[self.program[self.ptr + 1]]
            case 5: self.ptr = params[1] if params[0] != 0 else self.ptr
            case 6: self.ptr = params[1] if params[0] == 0 else self.ptr
            case 7: self.program[self.program[self.ptr + 3]] = 1 if params[0] < params[1] else 0
            case 8: self.program[self.program[self.ptr + 3]] = 1 if params[0] == params[1] else 0
            case 99: status = 99
        if self.ptr == ptr_initial and status == None:
            self.ptr += vars_per_opcode[opcode] + 1
        return out, status

outs = []
for phase_settings in permutations([0, 1, 2, 3, 4]):
    amps = [amp(input_program.copy(), [phase_setting] if i > 0 else [phase_setting, 0]) for i, phase_setting in enumerate(phase_settings)]
    for i in range(5):
        status = None
        while status == None:
            out, status = amps[i].calc()
            if out != None:
                if i == 4:
                    outs.append(out)
                else:
                    amps[i+1].inputs.append(out)
print(max(outs))

outs = []
for phase_settings in permutations([5, 6, 7, 8, 9]):
    amps = [amp(input_program.copy(), [phase_setting] if i > 0 else [phase_setting, 0]) for i, phase_setting in enumerate(phase_settings)]
    i_amp = 0
    status = None
    while not (status == 99 and i_amp == 0):
        status = None
        while status == None:
            out, status = amps[i_amp].calc()
            if out != None:
                amps[i_amp+1].inputs.append(out) if i_amp < 4 else amps[0].inputs.append(out)
        i_amp = (i_amp + 1 if i_amp < 4 else 0)
    outs.append(amps[0].inputs[-1])
print(max(outs))