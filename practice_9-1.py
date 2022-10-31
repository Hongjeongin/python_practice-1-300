#201 함수 정의
def print_coin():
    print("비트코인")

#202 함수 호출
print_coin()

#203 함수 loop
for i in range(100):
    print_coin()

#204 함수 정의
def print_coins():
    for i in range(100):
        print_coin()

#206 실행 결과 예측 -> A B C A B
def message():
    print("A")
    print("B")
message()
print("C")
message()

#207 실행 결과 예측 -> A C B
print("A")
def message():
    print("B")
print("C")
message()


#208 실행 결과 예측 -> A C B E D
print("A")
def message1():
    print("B")
print("C")
def message2():
    print("D")
message1()
print("E")
message2()

#209 실행 결과 예측 -> B A
def message1():
    print("A")
def message2():
    print("B")
    message1()
message2()

#210 실행 결과 예측 -> B C B C B C A
def message2():
    print("B")
def message3():
    for i in range(3):
        message2()
        print("C")
    message1()
message3()
