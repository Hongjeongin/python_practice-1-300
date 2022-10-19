# 81-1 별 표현식
a, b, *c = (0, 1, 2, 3, 4, 5)

print(a)
print(b)
print(c)

#81-2 star expression 사용하여 왼쪽 8개 값 valid_score 변수에 바인딩
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)

#82 star expression 사용하여 오른쪽 8개 값 valid_score 변수에 바인딩
a, b, *valid_score = scores
print(valid_score)

#83 star expression 사용하여 가운데 8개 값 valid_score 변수에 바인딩
a, *valid_score, b = scores
print(valid_score)

#84 temp 이름의 비어있는 딕셔너리 만들기
temp = {}
print(temp)

#85 아이스크림 이름과 희망 가격을 딕셔너리로 구성
ice_cream = {"메로나":1000, "폴라포":1200, "빵빠레":1800}
print(ice_cream)

#86 아이스크림 추가
ice_cream["죠스바"] = 1200
ice_cream["월드콘"] = 1500
print(ice_cream)

#87 메로나 가격 출력
print("메로나 가격: {}".format(ice_cream["메로나"]))

#88 메로나 가격 수정
ice_cream["메로나"] = 1300
print(ice_cream)

#89 메로나 삭제
del ice_cream["메로나"]
print(ice_cream)