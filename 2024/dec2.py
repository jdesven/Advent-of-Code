import numpy as np
import pandas as pd

def test_if_safe(df_row):
    is_safe = True
    asc_desc_factor = 'asc' if df_row[0] < df_row[1] else 'desc'
    for j in range(len(df_row) - 1):
        if asc_desc_factor == 'asc' and df_row[j] >= df_row[j + 1]:
            is_safe = False
        if asc_desc_factor == 'desc' and df_row[j] <= df_row[j + 1]:
            is_safe = False
        if abs(df_row[j] - df_row[j + 1]) > 3:
            is_safe = False
    return is_safe

df = pd.read_csv('2024/input/dec2_input.csv', names = list(range(8)), delimiter = ' ')

# part 1
sum = 0
for i in range(len(df)):
    if test_if_safe(df.iloc[i].to_numpy()) == True:
        sum += 1
print('ans1: ' + str(sum))

# part 2
sum = 0
for i in range(len(df)):
    df_row = df.iloc[i].to_numpy()
    if test_if_safe(df_row) == True:
        sum += 1
    else:
        is_safe = False
        for j in range(len(df.columns)):
            if test_if_safe(np.delete(df_row, j)) == True:
                is_safe = True
        if is_safe == True:
            sum += 1
print('ans2: ' + str(sum))