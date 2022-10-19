#21 'p'와 't'만 출력
letters = 'python'

print(letters[0], letters[2])

#22 자동차 번호 뒷 4자리 출력
license_plate = "24가 2210"

print(license_plate.split()[1])
print(license_plate[-4:])

#23 문자열에서 '홀'만 출력
string = "홀짝" * 3 #홀짝홀짝홀짝

print(string[::2])

#24 문자열 거꾸로 뒤집어 출력
string = "PYTHON"

print(string[::-1])

#25 전화번호에서 하이푼('-')을 제거
phone_number = "010-1111-2222"

print(phone_number.replace("-", " "))

#26 25번의 전화번호를 붙여서 출력
print(phone_number.replace("-", ""))

#27 url에서 도메인 출력
url = "http://sharebook.kr"
print(url.split(".")[1])
print(url.split(".")[-1])

#29 소문자 a를 대문자 A로
string = 'abcdefa2a'
print(string.replace('a', 'A'))

#30 문자열은 불변
string = 'abcd'
string.replace('b', 'B')
print(string)