# 261
# 주식 종목 저장하는 Stock 클래스 정의 속성 메소드 X
class Stock:
    pass

# 262
# Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자 정의
class Stock_1:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        
    def printMySelf(self):
        print(f"이름: {self.name}, 코드: {self.code}")
        
samsung = Stock_1("삼성전자", "005930")
print("<262>")
samsung.printMySelf()

# 263
# 객체에 종목명을 입력할 수 있는 set_name 메소드 추가
class Stock_2(Stock_1):
    def set_name(self, name):
        self.name = name
    
a = Stock_2(None, None)
a.set_name("삼성전자")
print("<263>")
a.printMySelf()

# 264
# 객체에 종목코드를 입력할 수 있는 set_code 메소드 추가
class Stock_3(Stock_2):
    def set_code(self, code):
        self.code = code
        
a = Stock_3(None, None)
a.set_code("005930")
print("<264>")
a.printMySelf()

# 265
# 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.
class Stock_4(Stock_3):
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

samsung = Stock_4("삼성전자", "005930")
print("<265>")
print(f"이름: {samsung.get_name()}")
print(f"코드: {samsung.get_code()}")

# 266
# 생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요. PER, PBR, 배당수익률은 float 타입입니다.

class Stock_5(Stock_4):
    def __init__(self, name, code, per, pbr, revenue: float) -> None:
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.revenue = revenue
        
    def printMySelf(self):
        print(f"이름: {self.name}")
        print(f"코드: {self.code}")
        print(f"PER: {self.per}")
        print(f"PBR: {self.pbr}")
        print(f"배당수익률: {self.revenue}")
        
samsung = Stock_5("삼성전자", "005930", 15.79, 1.33, 2.83)
print("<266>")
samsung.printMySelf()