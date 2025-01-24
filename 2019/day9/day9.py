from pyhelper.pyimport import seperator_to_list_to_dict
program = seperator_to_list_to_dict('2019/input/day9_input.txt', seperator = ',', cast = int)
                    
class intcode:
    ptr = 0
    ptr_inputs = 0
    relative_offset = 0

    def __init__(self, program: dict, starting_inputs: list):
        self.program = program
        self.inputs = starting_inputs

    def get_var_pos_mode(self, mode_ptr: int):
        return self.program[mode_ptr]
    
    def get_var_imm_mode(self, mode_ptr: int):
        return mode_ptr
    
    def get_var_rel_mode(self, mode_ptr: int):
        return self.program[mode_ptr] + self.relative_offset

    def calc_step(self):
        vars_per_opcode = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 0}
        ptr_initial = self.ptr
        out = None
        status = None
        modes = str(self.program[self.ptr])[-3::-1]
        opcode = self.program[self.ptr] % 100
        stuffed_modes = ''.join([modes, '0' * (vars_per_opcode[opcode] - len(modes))])
        map_mode_to_func = {'0': self.get_var_pos_mode, '1': self.get_var_imm_mode, '2': self.get_var_rel_mode}
        locs = [map_mode_to_func[var](self.ptr + i_var) for i_var, var in enumerate(stuffed_modes, start = 1)]
        for loc in locs:
            if loc not in self.program.keys():
                self.program[loc] = 0

        match opcode:
            case 1: # addition
                self.program[locs[2]] = self.program[locs[0]] + self.program[locs[1]]
            case 2: # multiplication
                self.program[locs[2]] = self.program[locs[0]] * self.program[locs[1]]
            case 3: # take input
                if self.ptr_inputs < len(self.inputs):
                    self.program[locs[0]] = self.inputs[self.ptr_inputs]
                    self.ptr_inputs += 1
                else:
                    status = 3
            case 4: # output
                out = self.program[locs[0]]
            case 5: # jump-if-true
                self.ptr = self.program[locs[1]] if self.program[locs[0]] != 0 else self.ptr
            case 6: # jump-if-false
                self.ptr = self.program[locs[1]] if self.program[locs[0]] == 0 else self.ptr
            case 7: # less-than
                self.program[locs[2]] = 1 if self.program[locs[0]] < self.program[locs[1]] else 0
            case 8: # equals
                self.program[locs[2]] = 1 if self.program[locs[0]] == self.program[locs[1]] else 0
            case 9: # adjust relative offset
                self.relative_offset += self.program[locs[0]]
            case 99: # terminate
                status = 99
        if self.ptr == ptr_initial and status == None:
            self.ptr += vars_per_opcode[opcode] + 1
        return out, status

    def print_until_terminate(self):
        last_status = None
        while last_status != 99:
            out, last_status = self.calc_step()
            if out != None:
                print(out)

intcode(program.copy(), [1]).print_until_terminate()
intcode(program.copy(), [2]).print_until_terminate()