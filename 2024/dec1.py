import pandas as pd

df = pd.read_csv('2024/input/dec1_input.csv', names = ['left', 'right'], delimiter = '   ', engine = 'python')
df_left = df['left'].sort_values(ignore_index=True)
df_right = df['right'].sort_values(ignore_index=True)

# part 1
sum = 0
for i in range(len(df)):
    sum += abs(df_left[i] - df_right[i])
print('answer 1: ' + str(sum))

# part 2
sum = 0
for i in range(len(df)):
    sum += df_left[i] * len(df_right[df_right == df_left[i]])
print('answer 2: ' + str(sum))