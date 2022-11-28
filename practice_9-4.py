# 231
# 아래 코드 실행 결과 예상
result = 0
def n_plus_1(n):
    print("<232>")
    result = n + 1
n_plus_1(3)
print(f"result = {result}")

# 232
# 문자열 하나 입력 받아 인터넷 주소를 반환하는 함수 정의
def make_url(url: str):
    print("<232>")
    new_url = "www." + url + ".com"
    return new_url
print(make_url("naver"))

# 233
# 문자열 입력 받아 문자들 출력
def make_list(string: str):
    print("<233>")    
    new_list = []
    for cur_word in string:
        new_list.append(cur_word)
    return new_list
print(make_list("abcd"))

# 234
# 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 함수 구현
def pickup_even(num_list: list):
    print("<234>")
    even_num_list = []
    for num in num_list:
        if num % 2 == 0:
            even_num_list.append(num)
    return even_num_list
print(pickup_even([3, 4, 5, 6, 7, 8]))

# 235
# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의
def convert_int(num_with_comma: str):
    print("<235>")
    result = ''
    for cur_num in num_with_comma:
        if cur_num == ",":
            continue
        result += cur_num
    return result
print(convert_int("1,234,567"))
    
# 236
# 아래 코드 실행 결과 예측
def my_function(num):
    return num + 4
a = my_function(10)
b = my_function(a)
c = my_function(b)
print("<236>")
print(c)

# 237
# 아래 코드 실행 결과 예측
def my_function(num):
    return num + 4
c = my_function(my_function(my_function(10)))
print("<237>")
print(c)

# 238
# 아래 코드 실행 결과 예측
def function1(num):
    return num + 4

def function2(num):
    return num * 10

a = function1(10)
c = function2(a)
print("<238>")
print(c)

# 239
# 아래 코드 실행 결과 예측
def function1(num):
    return num + 4
def function2(num):
    num += 2
    return function1(num)
c = function2(10)
print("<239>")
print(c)

# 240
# 아래 코드 실행 결과 예측
def function0(num):
    return num * 2
def function1(num):
    return function0(num + 2)
def function2(num):
    num += 10
    return function1(num)

c = function2(2)
print("<240>")
print(c)








