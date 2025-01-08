with open('2024/input/dec1_input.txt', 'r') as file:
    nums = [[int(num.split('   ')[0]), int(num.split('   ')[1])] for num in [nums for nums in file.read().splitlines()]]

nums_left = sorted([row[0] for row in nums])
nums_right = sorted([row[1] for row in nums])

# part 1
print(sum([abs(nums_left[i] - nums_right[i]) for i in range(len(nums))]))

# part 2
print(sum(nums_left[i] * nums_right.count(nums_left[i]) for i in range(len(nums))))