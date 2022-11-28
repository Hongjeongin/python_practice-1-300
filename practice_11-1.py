# 251
# 클래스, 객체, 인스턴스에 대해 설명해봅시다.
print("<251>")
print("클래스: 공통적인 속성이나 행위를 갖는 객체들을 하나의 대상으로 추상화 한 것")
print("객체: 현실세계에 존재하는 유-무형의 모든 것")
print("인스턴스: 클래스로 만들어져 메모리상에 존재하는 객체")

# 252
# 비어있는 사람 클래스 정의
print("<252>")
class Human:
    def __init__(self, crying_word = None,name = None, age = None, sex = None):
        if crying_word == None:
            self.crying_word = "헤응"
        else:
            self.crying_word = crying_word
        if name == None:
            self.name = "noname"
        else:
            self.name = name
        if age == None:
            self.age = "0"
        else:
            self.age = age
        if sex == None:
            self.sex = "불명"
        else:
            self.sex = sex
        print(f"제 이름은 {self.name}이고 {self.age}살, 성별은 {self.sex}입니다. {self.crying_word}")
    def __del__(self):
        print("나의 죽음을 알리지 말라")
    def who(self):
        print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.sex}")
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
print("class Human(): pass")

# 253
# 사람 클래스의 인스턴스를 생성하고 이를 areum 변수로 바인딩 해보세요.
print("<253>")
areum = Human()
print(f"areum: {areum}")

# 254
# 사람 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.
print("<254>")
crying_word = "응애응애"
areum = Human(crying_word)

# 255
# 사람 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.
print("<255>")
areum = Human(crying_word, "홍정인", 26, "남자")

# 256
# 255에서 생성한 인스턴스의 (이름, 나이, 성별) 출력 인스턴스 변수에 접근하여 값 출력
print("<256>")
print(f"이름: {areum.name}, 나이: {areum.age}, 성별: {areum.sex}")

# 257
# 사람 클래스에서 (이름, 나이, 성별) 출력 메소드 추가
print("<257>")
areum.who()

# 258
# 사람 클래스에 (이름, 나이, 성별) 설정 메소드 추가
print("<258>")
areum.setInfo("아름", 25, "여자")
areum.who()

# 259
# 소멸자 추가
print("<259>")
del(areum)

# 260