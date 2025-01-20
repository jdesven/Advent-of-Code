[Link to puzzle](https://adventofcode.com/2019/day/5)\
[Previous Intcode puzzle](https://github.com/jdesven/Advent-of-Code/blob/5b1c5c37e3d3673eac6729ff14dcd3bcc9d27b38/2019/day2/README.md)
## Import

```python
from pyhelper.pyimport import seperator_to_list
program = seperator_to_list('2019/input/day5_input.txt', seperator = ',', cast = int)
```

# Solution

We store the amount of variables expected per opcode in `vars_per_opcode`. This dictionary is later used to determine how many steps the pointer `ptr` needs to move after executing an opcode operation.

We loop the Intcode program continuously using a `while True` loop, until we reach the `return` statement at opcode 99. For each cycle, we determine which mode (position or immediate, represented by 0 or 1, respectively) needs to be used for each parameter, and we save this in `modes`. Since any leading zeros are trimmed away in the input file, we need to add leading zeros to `modes` until the length of `modes` equals the amount of arguments expected for that opcode. We store the result in `stuffed_modes`. Then, for every argument, we pull the value of the argument from either the given position or directly as that number (depending on the mode) and store the result in `params`.

Whenever we hit an opcode 4 we overwrite `last_out` with that value, and ultimately output it when we hit opcode 99. Unless the pointer has already been changed this opcode operation (i.e. opcode 5 or 6), we move the pointer based on the amount of arguments in this opcode, as listed in `vars_per_opcode`.

``` python
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
```

This Intcode function incorporates both parts of the problem. To obtain the solutions to part 1 and 2, we call the function with inputs 1 and 5, respectively.

```python
print(run_opcode(program.copy(), 1))
print(run_opcode(program.copy(), 5))
```