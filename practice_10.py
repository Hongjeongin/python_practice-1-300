import datetime as dt
import numpy
import os

# 241
# datetime 모듈 사용해서 현재 시간 출력
print("<241>")
print(dt.datetime.now())

# 242
# datetime 모듈의 now 함수 리턴 값 타입 출력
print("<242>")
now = dt.datetime.now()
print(f"type: {type(now)}")

# 243
# timedelta 사용 오늘부터 5, 4, 3, 2, 1일 전의 날짜 출력
print("<243>")
for day in range(5, 0, -1):
    delta = dt.timedelta(days = day)
    date = now - delta
    print(f"{day}일 전 날: {date}")

# 244
# 현재시간 포멧 hh:mm:ss
print("<244>")
print(now.strftime("%H:%M:%S"))

# 245
# 문자열을 시간 타입으로 변환
print("<245>")
cur_time = "2020-05-04"
time_type_of_cur_time = dt.datetime.strptime(cur_time, "%Y-%M-%d")
print(cur_time)
print(f"원래의 타입: {type(cur_time)}")
print(f"바뀐 타입: {type(time_type_of_cur_time)}")

# 246
# 1초에 한 번 현재 시간 출력
print("<246>")
t = 0

while (t < 10):
    now = dt.datetime.now()
    print(now)
    t += 1

# 247
# 모듈을 import 하는 4가지 방식 설명
print("<247>")
print("모듈을 import 하는 4가지 방식")
print("import [모듈명]")
print("import [모듈명] as [사용할 이름]")
print("from [모듈명] import [함수명]")
print("from [모듈명] import *")

# 248
# os 모듈의 getcwd 함수 호출 - 현재 디렉토리 경로 출력
print("<248>")
print(f"현재 경로: {os.getcwd()}")

# 249
# 바탕화면에 텍스트 파일 하나 생성 후 이름 변경 - os의 rename() 함수
print("<249>")

# 250
# numpy모듈의 arange() 함수 사용 - 0.0부터 5.0까지 0.1씩 증가 값 출력
print("<250>")
for i in numpy.arange(0, 5, 0.1):
    print(i)