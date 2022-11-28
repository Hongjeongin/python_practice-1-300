# 221
# 입력된 문자열을 역순으로 출력하는 함수 정의
def print_reserve(string: str):
    print("<221번>")
    return string[::-1]
print(print_reserve("python"))

# 222
# 성적 리스트를 입력 받아 평균을 출력하는 함수 정의
def print_scores(score_arr: list):
    print("<222번>")
    sum_score = 0
    average = 0
    for score in score_arr:
        sum_score += score
    average = sum_score / len(score_arr)
    return average
print(print_scores([1, 3, 5]))

# 223
# 하나의 리스트를 입력받아 짝수만 출력
def print_even(num_list: list):
    print("<223번>")
    for num in num_list:
        if num % 2 == 0:
            print(num)
print_even([1, 3, 2, 10, 12, 11, 15])

# 224
# 하나의 딕셔너리 입력받아 딕셔너리 key 값 출력
def print_keys(people_dict: dict):
    print("<224번>")
    for person_info in people_dict.keys():
        print(person_info)
print_keys({"이름": "김말똥", "나이": 30,"성별": 0})

# 225
# my_dict와 날짜 키값을 입력받아 OHLC 리스트 출력하는 함수 정의
my_dict = {
    "10/26": [100, 130, 100, 100],
    "10/27": [10, 12, 10, 11]
}
def print_value_by_key(my_dict: dict, date: str):
    print("<225번>")
    ohlc = my_dict.get(date)
    print(ohlc)
print_value_by_key(my_dict, "10/26")

# 226
# 입력 문자열을 한 줄에 다섯글자씩 출력하는 함수 정의
def print_5xn(string: str):
    print("<226>")
    check_num = 5
    point = int((len(string)) / check_num)
    
    for i in range(point + 1):
        print(string[i * check_num: i * check_num + check_num])
print_5xn("아이엠어보이유알어걸")

# 227
# 문자열과 한 줄에 출력될 글자 수를 입력 받아 한 줄에 입력된 글자 수만큼 출력하는 함수 정의
def print_mxn(string: str, check_num: int):
    print("<227>")
    point = int((len(string)) / check_num)
    for i in range(point + 1):
        print(string[i * check_num: i * check_num + check_num])
print_mxn("아이엠어보이유알어걸", 3)

# 228
# 연봉을 입력받아 월급을 계샇나는 함수 정의 - 12개월 분할 지급, 1월 미만 = 버림

def calc_mothly_salary(annual_salary: int):
    print("<228>")
    month_salary = annual_salary / 12
    final_month_salary = int(month_salary / 10) * 10
    print(f"해당 직원의 월급은 {final_month_salary}원 입니다.")
calc_mothly_salary(12000001)

# 229 - 230
# 아래 코드의 실행 결과를 예측하라
def my_print(console, a, b):
    print(console)
    print("left", a)
    print("right", b)
my_print("<229>", a = 100, b = 200)
my_print("<230>", b = 100, a = 200)