with open('2019/input/dec2_input.txt', 'r') as file:
    input = [int(num) for num in file.read().split(',')]

def calculate_output(input, noun, verb):
    mod_input = [input[0]] + [noun] + [verb] + input[3:]
    for i in range (0, len(input), 4):
        match mod_input[i]:
            case 1:
                mod_input[mod_input[i + 3]] = mod_input[mod_input[i + 1]] + mod_input[mod_input[i + 2]]
            case 2:
                mod_input[mod_input[i + 3]] = mod_input[mod_input[i + 1]] * mod_input[mod_input[i + 2]]
            case 99:
                return mod_input[0]

# part 1
print(calculate_output(input, 12, 2))

# part 2
for noun in range(100):
    for verb in range(100):
        if calculate_output(input, noun, verb) == 19690720:
            print(100 * noun + verb)