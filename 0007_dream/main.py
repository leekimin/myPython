import pandas as pd
import sys, json, time, pprint

print('-' * 50, 'start')
print('params : birth, dream keyword, ')

data_file_name = 'dream.csv'

dream_csv = pd.read_csv(
    data_file_name, 
    encoding='UTF-8', 
    header=0,
    index_col=0, 
    usecols=[0, 1, 2, 3, 4, 5, 6, 7]
)

# column place
# dream_csv.rename(columns={"회차":"no", "번호1":"no1"}, inplace=True)
print(len(dream_csv))
#print(dream_csv.loc[dream_csv.index == 1095]) # index value check

#for row in enumerate(dream_csv):
#    print(row)

lstSer = []

for idx, ser in dream_csv.iterrows():
    print('-' * 40, idx)
    print(ser["no1"])
    if idx == 1097:
        break;


print('-' * 50, 'end')

"""
https://github.com/onlybooks/python-algorithm-interview?tab=readme-ov-file
"""