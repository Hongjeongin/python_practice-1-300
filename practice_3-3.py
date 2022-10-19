#41 문자열을 대문자로 변환
ticker = "btc_krw"
ticker_up = ticker.upper()
print(ticker_up)

#42 문자열을 소문자로 변환
print(ticker_up.lower())

#43 capitalize 메소드,, hello -> Hello
hello = "hello"
print(hello.capitalize())

#44 endswith 메소드,, 파일 이름이 xlsx로 끝나는지 확인
fileName = "보고서.xlsx"
print(fileName.endswith("xlsx"))

#45 파일 이름이 xlsx 또는 xls로 끝나는지 확인
print(fileName.endswith(("xlsx", "xls")))

#46 startswith 메소드,, 파일 이름이 2020으로 시작하는지 확인
fileName = "2020_보고서.xlsx"
print(fileName.startswith("2020"))

#47 공백 기준으로 나누기
a = "hello world"
print(a.split())

#48 언더바 기준으로 나누기
ticker = "btc_krw"
print(ticker.split("_"))

#49 년 월 일 나누기
date = "2020-05-01"
print(date.split("-"))

#50 rstrip 메소드
data = "031340      "
print(data.rstrip())