#91 딕셔너리 생성
inven = {"메로나":[300, 20], "비비빅":[400, 3], "죠스바":[250, 100]}
print(inven)

#92 메로나 가격
print("{} 원".format(inven["메로나"][0]))

#93 메로나 재고
print("{} 원".format(inven["메로나"][1]))

#94 딕셔너리 추가
inven["월드콘"] = [500, 7]
print(inven)

#95 keys() 메소드
ice_list = list(inven.keys())
print(ice_list)

#96 values() 메소드
ice_values = list(inven.values())
print(ice_values)

#97 판매 금액 촘합 출력
ice_cream = {
    '탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500,
    '메로나': 1000
}
ice_price = sum(ice_cream.values())
print(ice_price)

#98 딕셔너리 추가
new_product = {'팥빙수': 2700, '아맛나': 1000}
ice_cream.update(new_product)
print(ice_cream)

#99 튜플을 딕셔너리로 만들기
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)

result = dict(zip(keys, vals))

print(result)

#100 리스트를 딕셔너리로 만들기
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price))
print(close_table)