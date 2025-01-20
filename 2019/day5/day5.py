from pyhelper.pyimport import seperator_to_list
program = seperator_to_list('2019/input/day5_input.txt', seperator = ',', cast = int)

def run_opcode(program, user_input):
    vars_per_opcode = {1: 3, 2: 3, 3: 1, 4: 1, 99: 0, 5: 2, 6: 2, 7: 3, 8: 3}
    ptr = 0
    while True:
        modes = str(program[ptr])[-3::-1]
        opcode = program[ptr] % 100
        stuffed_modes = ''.join([modes, '0' * (vars_per_opcode[opcode] - len(modes))])
        params = [program[program[ptr + i_var]] if var == '0' else program[ptr + i_var] for i_var, var in enumerate(stuffed_modes, start = 1)]
        ptr_initial = ptr
        match opcode:
            case 1: program[program[ptr + 3]] = params[0] + params[1]
            case 2: program[program[ptr + 3]] = params[0] * params[1]
            case 3: program[program[ptr+1]] = user_input
            case 4: last_out = program[program[ptr + 1]]
            case 5: ptr = params[1] if params[0] != 0 else ptr
            case 6: ptr = params[1] if params[0] == 0 else ptr
            case 7: program[program[ptr + 3]] = 1 if params[0] < params[1] else 0
            case 8: program[program[ptr + 3]] = 1 if params[0] == params[1] else 0
            case 99: return last_out
        if ptr == ptr_initial:
            ptr += vars_per_opcode[opcode] + 1

print(run_opcode(program.copy(), 1))
print(run_opcode(program.copy(), 5))