[Link to puzzle](https://adventofcode.com/2019/day/2)
## Import

```python
from pyhelper.pyimport import seperator_to_list
input = seperator_to_list('2019/input/day2_input.txt', seperator = ',', cast = int)
```

## Solution
We can iterate the pointer `i` from 0 to the length of the input with steps of 4, since both opcodes 1 and 2 move the pointer four spaces after execution and no backtracking is possible (yet). With the specific noun and verb, we find the answer to the first part.

```python
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
print(calculate_output(input, 12, 2))
```

To find the answer to the second part, we try all options for nouns and verbs in the range [0,99]. Since we only need to try 10,000 combinations, this method is fast enough.

```python
for noun in range(100):
    for verb in range(100):
        if calculate_output(input, noun, verb) == 19690720:
            print(100 * noun + verb)
```