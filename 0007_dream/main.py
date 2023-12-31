import pandas as pd
from collections import Counter
import sys, json, time, pprint, re

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
lstBonus = []

for idx, ser in dream_csv.iterrows():
    lstSer.append(ser["no1"])
    lstSer.append(ser["no2"])
    lstSer.append(ser["no3"])
    lstSer.append(ser["no4"])
    lstSer.append(ser["no5"])
    lstSer.append(ser["no6"])
    lstBonus.append(ser["no7"])

print('-' * 30)
cnter = Counter(lstSer)
#print(cnter.most_common(1)[0][0])

print('-' * 30)
bnCnter = Counter(lstBonus)
#print(bnCnter.most_common(1)[0][0])

print('-' * 50, 'end')

"""
https://github.com/onlybooks/python-algorithm-interview?tab=readme-ov-file
"""

# dream 별 숫자 데이터 수집...
str = """
        한글[123][11][22][33]★★★★
    """
strRegx = r'(\w+)+([\[+\d+\]]+)?+(\★+)?';
p = re.compile(strRegx)

strMatch = re.findall(strRegx, str)
# print(strMatch)

rx = r'\[+(\d+)+\]'

# keyword로 데이터 정리
for m in strMatch:
    print('-' * 30, m)
    if len(m) != 3:
        print('continue ', m)
    
    # key, num, weight
    stmp = re.findall(rx, m[1])
    print('key =', m[0])
    print('num =', stmp)
    print('wgt =', m[2])


