import csv
# 291
# 바탕화면에 '매수종목1.txt' 파일을 생성한 후 다음과 같이 종목코드를 파일에 써보세요.
print("<291>")
f = open("./매수종목1.txt", mode="wt", encoding="utf-8")

f.write("005930\n")
f.write("005380\n")
f.write("035420")

f.close()

# 292
# 바탕화면에 '매수종목2.txt' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요.
items = {"005930": "삼성전자", "005380": "현대차", "035420": "NAVER"}
print("<292>")
f = open("./매수종목2.txt", mode="wt", encoding="utf-8")

for i, item in enumerate(items):
    cur_text = f"{list(items.values())[i]} {list(items.keys())[i]}\n"
    f.write(cur_text)

f.close()

# 293
# 바탕화면에 '매수종목.csv' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요. 인코딩은 'cp949'를 사용해야합니다.
items = {
    "one": ["종목명", "종목코드", "PER"],
    "two": ["삼성전자", "005930", 15.79],
    "three": ["NAVER", "035420", 55.82],
}

f = open("./매수종목.csv", mode="wt", encoding="utf-8", newline='')
print("<293>")

writer = csv.writer(f)

for i in range(len(items)):
    writer.writerow(list(items.values())[i])
    
f.close()

# 294
# 바탕화면에 생성한 '매수종목1.txt' 파일을 읽은 후 종목코드를 리스트에 저장해보세요.
f = open("매수종목1.txt", encoding="utf-8")
lines = f.readlines()

codes = []
for line in lines:
    code = line.strip()
    codes.append(code)
    
print("<294>")
print(codes)

f.close()

# 295
# 바탕화면에 생성한 '매수종목2.txt' 파일을 읽은 후 종목코드와 종목명을 딕셔너리로 저장해보세요. 종목명을 key로 종목명을 value로 저장합니다.
f = open("매수종목2.txt", encoding="utf-8")
lines = f.readlines()

items = {}
for line in lines:
    line = line.strip()
    k, v = line.split()
    items[k] = v

print("<295>")
print(items)

f.close()

# 296
# 문자열 PER (Price to Earning Ratio) 값을 실수로 변환할 때 에러가 발생합니다. 예외처리를 통해 에러가 발생하는 PER은 0으로 출력하세요.
per = ["10.31", "", "8.00"]

print("<296>")
for i in per:
    try:
        print(float(i))
    except:
        print(0)
        
# 297
# 문자열로 표현된 PER 값을 실수로 변환한 후 이를 새로운 리스트에 저장해보세요.

per_list = []

for i in per:
    try:
        per_list.append(float(i))
    except:
        per_list.append(0)

print("<297>")
print(per_list)

# 298
# 어떤 값을 0으로 나누면 ZeroDivisionError 에러가 발생합니다. try ~ except로 모든 에러에 대해 예외처리하지 말고 ZeroDivisionError 에러만 예외처리해보세요.
num = 1
division = 0
print("<298>")
try:
    division = 1 / 0
except(ZeroDivisionError):
    print("0으로는 나눌 수 없습니다...")
    
# 299
# 다음과 같은 코드 구조를 사용하면 예외 발생 시 에러 메시지를 변수로 바인딩할 수 있습니다.
data = [1, 2, 3]

print("<299>")
for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

# 300
# 파이썬 예외처리는 다음과 같은 구조를 가질 수 있습니다.
per_list = []
print("<300>")
for i in per:
    try:
        per_list.append(float(i))
    except:
        per_list.append(0)
    else:
        print(f"{i} casting success")
    finally:
        print(f"{i} append success")
        
print(per_list)