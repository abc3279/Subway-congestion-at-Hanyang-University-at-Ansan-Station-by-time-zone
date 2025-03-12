import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('subway.csv', encoding='cp949')
# print(file.columns)
# print(file.head())

file = file[file.columns[:-1]] # 작업일자 없애기
file = file[file["사용월"] >= 202310] # 2023년 10월 데이터로만 재구성.
file = file[file["호선명"]  == '안산선'] # 안산선으로만 재구성.

file = file[file["지하철역"] == '한대앞']   # 한대앞역으로만 재구성
# print(file.head())

indexList = []
numberList = []

for i in range(3, len(file.columns), 2): # 승차 인원 + 하차인원
    vs_index_f = file.columns[i]
    vs_index_s = file.columns[i+1]

    vs = ((file[file["지하철역"] == "한대앞"])[vs_index_f].values)[0] + ((file[file["지하철역"] == "한대앞"])[vs_index_s].values)[0]
    
    indexList.append(vs_index_f[0:2] + '~' + vs_index_f[4:6])
    numberList.append(vs)

numberDict = {'Subway Congestion': numberList}


l = pd.DataFrame(numberDict, index=indexList)

print(l)

l.plot(kind='bar', color=('m'))
plt.show()
