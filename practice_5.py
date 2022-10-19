#71 비어있는 튜플 만들기
my_variable = ()
print(type(my_variable))

#72 영화 제목을 튜플에 저장
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

#73 숫자 1만 저장된 튜플 생성
tuple_1 = (1, )
print(tuple_1)

#74 튜플은 원소 값 변경 X

#75 t 데이터 타입
t = 1, 2, 3, 4
print(t, type(t))

#76 튜플 수정
t = ('a', 'b', 'c')
print(t)
t = ('A', 'b', 'c')
print(t)

#77 튜플 -> 리스트
interest = ('삼성전자', 'LG전자', 'SH Hynix')
inter_list = list(interest)
print(inter_list)

#78 리스트 -> 튜플
inter_tuple = tuple(inter_list)
print(inter_tuple)

#79 튜플 언팩킹
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

#80 range 함수 1 ~ 99 중 짝수만 저장된 튜플
data = tuple(range(2, 100, 2))
print(data)