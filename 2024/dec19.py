towels, patterns = open('2024/input/dec19_input.txt', 'r').read().split('\n\n')

def count_combinations(pattern, towels):
    pattern_parts_counts = {}
    for i in range(len(pattern) + 1):
        pattern_parts_counts[pattern[:i]] = 0 if i > 0 else 1
    for pattern_part in pattern_parts_counts:
        for towel in towels:
            if pattern_part + towel in pattern_parts_counts:
                pattern_parts_counts[pattern_part + towel] += pattern_parts_counts[pattern_part]
    return pattern_parts_counts[pattern]

#part 1
print('ans1: ' + str(sum([1 if count_combinations(pattern,towels.split(', ')) > 0 else 0 for pattern in patterns.split('\n')])))

# part 2
print('ans2: ' + str(sum([count_combinations(pattern,towels.split(', ')) for pattern in patterns.split('\n')])))