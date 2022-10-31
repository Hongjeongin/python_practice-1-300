#211 결과 예측 -> 안녕 Hi
def func(msg):
    print(msg)
func("안녕")
func("Hi")

#212 결과 예측 -> 7 15
def func_add(a, b):
    print(a + b)
func_add(3, 4)
func_add(7, 8)

#213 에러 원인 설명 -> argument issue

#214 에러 원인 설명 -> 잘못된 argument 입력

#215 스마일 함수
def print_with_smile(msg):
    print(msg + ":D")

#216 스마일 호출
print_with_smile("안녕하세요")

#217 상한가 출력 함수
def print_upper_price(cur_price):
    print(cur_price + (cur_price * 0.3))

#218 합 출력 함수
def print_sum(a, b):
    print(a + b)

#219 합 차 곱 나눗셈 함수
def print_arithmetic_operation(a, b):
    if b <= 0:
        return {print("wrong")}
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
print_arithmetic_operation(3, 5)

#220 가장 큰 수
def print_max(num1, num2, num3):
    MAX_STR = "max num is: "
    if num1 >= num2 and num1 >= num3:
        print(MAX_STR, num1)
    elif num2 >= num3:
        print(MAX_STR, num2)
    else:
        print(MAX_STR, num3)
print_max(3, 4, 5)