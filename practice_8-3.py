#151
num_list = [3, -20, -3, 44]
for val in num_list:
    if val < 0:
        print(val)

#152 3의 배수
num_list = [3, 100, 23, 44]
for val in num_list:
    if val % 3 == 0:
        print(val)

#153 3의 배수
num_list = [13, 21, 12, 14, 30, 18]
for val in num_list:
    if val < 20 and val % 3 == 0:
        print(val)
    
#154 3글자 이상 출력
str_list = ["I", "study", "python", "language", "!"]
for val in str_list:
    if len(val) >= 3:
        print(val)

#155 대문자 출력
alphabet = ["A", "b", "c", "D"]
for val in alphabet:
    if val.isupper():
        print(val)

#156 소문자 출력
for val in alphabet:
    if val.islower():
        print(val)

#157 첫글자 변경
animals = ['dog', 'cat', 'parrot']
for val in animals:
    upper_val =  val.replace(val[0], val[0].upper())
    print(upper_val)

#158 확장자 제거
files = ['hello.py', 'ex01.py', 'intro.hwp']
for val in files:
    print(val.split(".")[0])

#159 확장자 색출
files = ['intra.h', 'intra.c', 'define.h', 'run.py']
for val in files:
    if val.split(".")[1] == "h":
        print(val)

#160 확장자 색출
for val in files:
    extension = val.split(".")[1]
    if extension == "h" or extension == "c":
        print(val)