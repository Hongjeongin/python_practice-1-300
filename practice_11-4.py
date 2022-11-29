# 281
# 다음 코드가 동작하도록 차 클래스를 정의하세요.
class Car:
    def __init__(self, _tires, _price):
        self._tires = _tires
        self._price = _price
    
    def tires(self):
        print(self._tires)
    
    def price(self):
        print(self._price)
        
    def information(self):
        print(f"바퀴수: {self._tires}")
        print(f"가격: {self._price}")

print("<281>")

# 282
# 차 클래스를 상속받은 자전차 클래스를 정의하세요.
class Bicycle(Car):
    def __init__(self, _tires, _price, _drive_train = None):
        self._tires = _tires
        self._price = _price
        self._drive_train = _drive_train
    
    def drive_train(self):
        print(self._drive_train)        
    
    def information(self):
        super().information()
        print(f"구동계: {self._drive_train}")

print("<282>")

# 283
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
print("<283>")
bike = Bicycle(2, 100)
bike.price()

# 284
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
print("<284>")
bike = Bicycle(2, 100, "시마노")
bike.drive_train()

# 285
# 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.
class Car1(Car):
    pass
print("<285>")
car = Car1(4, 1000)
car.information()

# 286
# 다음 코드가 동작하도록 차 클래스를 수정하세요.
print("<286>")
bike = Bicycle(2, 100, "시마노")
bike.information()

# 287
# 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.
print("<287>")

# 288
# 다음 코드의 실행 결과를 예상해보세요.
class Parent:
    def __init__(self):
        print("부모생성")
    def call(self):
        print("call parent")

class Child(Parent):
    def __init__(self):
        print("자식생성")
        super().__init__()
    def call(self):
        print("call child")
        
i = Child()
print("<288>")
i.call()

# 289
# 다음 코드의 실행 결과를 예상해보세요.
print("<289>")

# 290
# 다음 코드의 실행 결과를 예상해보세요.
print("<290>")