#221 문자열 역순 출력
def print_reverse(msg):
    print(msg[::-1])
print_reverse("python")

#222 평균 출력
def print_score(scores):
    result = 0
    for val in scores:
        result += val
    print(result / len(scores))
print_score([1, 2, 3])

#223 짝수 출력
def print_even(numbers):
    for val in numbers:
        if val % 2 == 0:
            print(val)
print_even([1, 3, 2, 10, 12, 11, 15])

#224 딕셔너리 키값 출력
def print_keys(dictionary):
    for val in dictionary.keys():
        print(val)
print_keys({"이름":"김말똥", "나이": 30, "성별": 0})

#225 OHLC 리스트 출력
def print_value_by_key(dict, date):
    print(dict[date])

my_dict = {"10/26":[100, 130, 100, 100],
           "10/27":[10, 12, 10, 11]}
print_value_by_key(my_dict, "10/26")