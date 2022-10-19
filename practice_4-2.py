#61 날짜 제외 가격정보만 출력
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#62 홀수 출력
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#63 짝수 출력
print(nums[1::2])

#64 역방향 출력
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#65 출력
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

#66 join 메소드
interest.append("하이닉스")
interest.append("미래에셋대우")

print(" ".join(interest))

#67 join 메소드
print("/".join(interest))

#68 join 메소드
print("\n".join(interest))

#69 분리 저장
string = "삼성전자/LG전자/Naver"

str_arr = string.split("/")
print(str_arr)

#70 오름차순
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()

print(data)