#141 부가세 포함 가격 출력
sell_list = [100, 200, 300]
for val in sell_list:
    print(val + 10)

#142 메뉴 출력
menu_list = ["김밥", "라면", "튀김"]
for val in menu_list:
    print("오늘의 메뉴: {}".format(val))

#143 문자열 길이 출력
brand = ["SK하이닉스", "삼성전자", "LG전자"]
for val in brand:
    print(len(val))

#144 동물 이름 + 글자수 출력
animals = ["dog", "cat", "parrot"]
for val in animals:
    print(val, len(val))

#145 동물 첫글자 출력
for val in animals:
    print(val[0])

#146 3의 배수 출력
num_list = [1, 2, 3]
for val in num_list:
    print("3 x {}".format(val))

#147 3의 배수 출력
for val in num_list:
    print("3 x {} = {}".format(val, val * 3))

#148 한글 출력
kor_list = ["가", "나", "다", "라"]
for i in range(1, 4):
    print(kor_list[i])

for val in kor_list[1:]:
    print(val)

#149 한글 출력
for val in kor_list[0::2]:
    print(val)

#150 역 출력
for val in kor_list[::-1]:
    print(val)