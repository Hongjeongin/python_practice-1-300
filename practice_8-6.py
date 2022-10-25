#181 아파트
apartment = [[101, 102], [201, 202], [301, 302]]
print(apartment)

#182 stock
stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]
print(stock)

#183 dict
stock_dict_1 = {"시가": [100, 200, 300], "종가": [80, 210, 330]}
print(stock_dict_1)

#184 dictionary
stock_dict_2 = {"10/10":[80, 110, 70, 90], "10/11":[210, 230, 190, 200]}
print(stock_dict_2)

#185 데이터 출력
for val in apartment:
    for i in range(2):
        print(val[i], "호")

for val in apartment[::-1]:
    for i in range(2):
        print(val[i], "호")

#187 데이터 출력
for val in apartment[::-1]:
    for i in range(len(val) - 1, -1, -1):
        print(val[i], "호")

#188 데이터 출력
for val in apartment:
    for i in range(2):
        print(val[i], "호")
        print("-----")

#189 데이터 출력
for val in apartment:
    for i in range(len(val)):
        print(val[i], "호")
    print("-----")

#190 데이터 출력
for val in apartment:
    for i in range(len(val)):
        print(val[i], "호")
print("-----")