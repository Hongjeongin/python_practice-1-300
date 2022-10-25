#191 수수료 포함 가격 출력
data = [
    [2000, 3050, 2050, 1980],
    [7500, 2050, 2050, 1980],
    [1540, 15050, 15550, 14900]
]
for val in data:
    for i in range(len(val)):
        print(val[i] + val[i] * 0.00014)

#192 191을 행단위로 출력
for val in data:
    for i in range(len(val)):
        print(val[i] + val[i] * 0.00014)
    print("----")

#193 192값 1차원 배열 저장
data_of_one_dimension = []
for val in data:
    for i in range(len(val)):
        data_of_one_dimension.append(val[i] + val[i] * 0.00014)
print(data_of_one_dimension)

#194 191값 2차원배열 정리
data_of_two_dimension = []
for val in data:
    current_array = []
    for i in range(len(val)):
        current_array.append(val[i] + val[i] * 0.00014)
    data_of_two_dimension.append(current_array)
print(data_of_two_dimension)

#195 종가 데이터 출력
ohlc = [
    ["open", "high", "low", "close"],
    [100, 110, 70, 100],
    [200, 210, 180, 190],
    [300, 310, 300, 310]
]
for i in range(1, len((ohlc[0]))):
    print(ohlc[i][-1])

#196 조건부 종가 출력
for i in range(1, len(ohlc[0])):
    cur_val = ohlc[i][-1]
    if cur_val > 150:
        print(cur_val)

#197 조건부 종가 출력
for i in range(1, len(ohlc[0])):
    cur_val = ohlc[i][-1]
    if cur_val >= ohlc[i][0]:
        print(cur_val)

#198 변동폭 저장
volatility = []
for i in range(1, len(ohlc[0])):
    cur_volat = ohlc[i][1] - ohlc[i][2]
    volatility.append(cur_volat)
print(volatility)

#199 변동성 출력
for i in range(1, len(ohlc[0])):
    high = ohlc[i][-1]
    low = ohlc[i][0]
    if high > low:
        print(high - low)

#200 수익금 계산
result = 0
for i in range(1, len(ohlc[0])):
    result += (ohlc[i][-1] - ohlc[i][0])
print(result)