#121 입력 값에 따른 출력
# awnser = input("문자 한 개 입력: ")
# print(awnser.upper() if awnser.islower() else awnser.lower())

#122 학점 출력
# awnser = input("score: ")
# if awnser > 80:
#     print("A")
# elif awnser > 60:
#     print("B")
# elif awnser > 40:
#     print("C")
# elif awnser > 20:
#     print("D")
# else:
#     print("E")

#123 환전
# awnser = input("돈 입력: ")
# exchange = {
#     "달러": 1167,
#     "엔": 1.096,
#     "유로": 1268,
#     "위안": 171
# }
# awn_s = awnser.split()
# print(int(awn_s[0]) * exchange[awn_s[1]])

#124 가장 큰 수
# num1 = input("숫자1 입력: ")
# num2 = input("숫자2 입력: ")
# num3 = input("숫자3 입력: ")

# numList = []
# numList.append(num1)
# numList.append(num2)
# numList.append(num3)

# maxNum = max(numList)
# print(maxNum)

#125 통신사 알아내기
# compony = {"011": "SKT", "016": "KT", "019": "LGU", "010": "알 수 없음"}

# phoneNum = input("휴대전화 번호 입력(form: 000-0000-0000): ")
# phone_first_num = phoneNum.split("-")[0]
# if phoneNum.split("-")[0] in compony.keys():
#     print(compony[phone_first_num])
# else:
#     print("존재하지 않아요..")

#126 우편번호 서울 [OO구] 판별
# postNum = input("우편번호: ")

# first_postNum = postNum[:3]

# if first_postNum in ["010", "011", "012"]:
#     print("강북구")
# elif first_postNum in ["013", "014", "015"]:
#     print("도봉구")
# elif first_postNum in ["016", "017", "018", "019"]:
#     print("노원구")
# else:
#     print("없어용..")

#127 주민등록번호 성별 판별
# personal_ID = input("주민등록번호(form: 000000-0000000): ")

# sex = personal_ID.split("-")[1][0]

# if sex in ["1", "3"]:
#     print("남자")
# elif sex in ["2", "4"]:
#     print("여자")
# else:
#     print("없는 성별")

#128 주민등록번호 지역코드 판별
# personal_ID = input("주민등록번호(form: 000000-0000000): ")

# local_code = int(personal_ID.split("-")[1][1:3])
# if 0 <= local_code < 9 :
#     print("서울입니다.")
# elif local_code < 13:
#     print("부산입니다.")
# else:
#     print("서울이 아닙니다.")

#129 주민등록번호 유효 판별
# personal_ID = input("주민등록번호(form: 000000-0000000): ")

# testNums = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

# personal_ID_str = personal_ID.replace("-", "")

# sum = 0
# result = 0

# for i in range(0, 12):
#     sum += int(personal_ID_str[i]) + testNums[i]

# result = sum % 11

# if result != int(personal_ID_str[-1]):
#     print("유효하지 않은 주민등록번호입니다.")
# else:
#     print("유효한 주민등록번호입니다.")

#130 시가 파악(상승장, 하락장)
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# difference = float(btc["opening_price"]) + float(btc["max_price"]) - float(btc["min_price"])
# print(btc)
# print(difference, btc["max_price"])
# if difference > float(btc["max_price"]):
#     print("상승장")
# else:
#     print("하락장")

