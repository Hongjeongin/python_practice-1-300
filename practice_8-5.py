#171 데이터 출력(for, range 사용)
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_list[i])

#172 데이터 출력(for, range 사용)
for i in range(4):
    print(i, price_list[i])

#173 데이터 출력(for, range 사용)
for i in range(4):
    print(3 - i, price_list[i])

#174 데이터 출력(for, range 사용)
for i in range(1, 4):
    print(100 + (i - 1) * 10, price_list[i])

#175 출력
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list) - 1):
    print(my_list[i], my_list[i + 1])

#176 출력
my_list.append("마")
for i in range(len(my_list) - 2):
    print(my_list[i], my_list[i + 1], my_list[i + 2])

#177 range 사용 출력
del my_list[-1]
print(my_list)
for i in range(len(my_list) - 1, 0, -1):
    print(my_list[i], my_list[i - 1])

#178 우측값 차분값 출력
my_list = [100, 200, 400, 800]
for i in range(len(my_list) - 1):
    print(my_list[i + 1] - my_list[i])

#179 데이터 평균 계산
my_list.append(1000)
my_list.append(1300)
for i in range(len(my_list) - 2):
    print((my_list[i] + my_list[i + 1] + my_list[i + 2]) / 3)

#180 변동폭 저장
low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(len(low_prices)):
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)