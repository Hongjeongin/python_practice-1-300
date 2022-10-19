#31 문자열 합치기
a = '3'
b = '4'
print (a + b)

#32 문자열 곱하기
print("Hi" * 3)

#33 화면에 '-'를 80개 출력
print('-' * 80)

#34 문자열 더하기 & 곱하기
t1 = 'python'
t2 = 'java'
print((t1 + " " + t2 + " ") * 4)

#35 % formatting
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

#36 format() 메소드 사용
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

#37 python3.6부터 지원하는 f-string 사용
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

#38 컴마 제거 후 정수로 변환
상장주식수 = "5,969,782,550"
sj = int(상장주식수.replace(",", ""))
print(sj, "=", type(sj))

#39 2020/03만 출력
분기 = "2020/03(E) (IFRS연결)"
slice분기 = 분기.split("(")[0]
print(slice분기)
print(분기[:7])

#40 strip 메소드
data = "    삼성전자    "
print(data.strip())