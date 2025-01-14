with open('2019/input/dec4_input.txt', 'r') as file:
    range_min, range_max = [int(num) for num in file.read().split('-')]

nums = set()
def calc_next_nums(num):
    if num == []:
        next_nums = range(1, 10)
    elif len(num) == 5 and len(num) == len(set(num)):
        next_nums = [num[-1]]
    else:
        next_nums = range(num[-1],10)

    if len(num) == 6:
        nums.add(int(''.join(map(str, num))))
    elif len(next_nums) > 0:
        for next_num in next_nums:
            calc_next_nums(num + [next_num])
            
calc_next_nums([])
print(len([num for num in nums if range_min <= num <= range_max]))