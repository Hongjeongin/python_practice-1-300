#161 0~99 출력
for i in range(0, 100):
    print(i)

#162 월드컵 개최 년도
for i in range(2002, 2051, 4):
    print(i)

#163 3의 배수
for i in range(1, 31):
    if i % 3 == 0:
        print(i)

#164 99~0
for i in range(99, -1, -1):
    print(i)

#165 소수 출력
for i in range(10):
    print(i / 10)

#166 구구단 3단
for i in range(1, 10):
    print("3 x {} = {}".format(i, i *3))

#167 구구단 3단 홀수
for i in range(1, 10, 2):
    print("3 x {} = {}".format(i, i * 3))

#168 1~10 더한 값
sum = 0
for i in range(1, 11):
    sum += i
print("합:", sum)

#169 홀수의 합
sum = 0
for i in range(1, 11, 2):
    sum += i
print("합:", sum)

#170 1~10 곱한 값
mul = 1
for i in range(1, 11):
    mul *= i
print("곱:", mul)