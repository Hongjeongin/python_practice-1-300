import random
import datetime as dt

# 271
# 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. Account 클래스를 생성한 후 생성자를 구현해보세요.
# 생성자에서는 예금주와 초기 잔액만 입력 받습니다. 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.

bank = "SC은행"

def make_account(customers_account_number):
    account_number = ''
    
    while(True):
        firstNum = random.randint(0, 999)
        secondNum = random.randint(0, 99)
        thirdNum = random.randint(0, 999999)
        
        firstNum = str(firstNum).zfill(3)
        secondNum = str(secondNum).zfill(2)
        thirdNum = str(thirdNum).zfill(6)
        
        account_number = firstNum + '-' + secondNum + '-' + thirdNum
        
        if account_number not in customers_account_number:
            break
        
    return account_number

class Account:
    customers_account_number = []
    account_count = 0
    
    def __init__(self, owner, balance) -> None:
        self.deposit_history = []
        self.withdraw_history = []
        self.deposit_count = 0
        self.owner = owner
        self.balance = balance
        self.bank = bank
        self.account_number = make_account(Account.customers_account_number)
        
        Account.customers_account_number.append(self.account_number)
        Account.account_count += 1  # 272
    
    @classmethod
    def get_account_num(cls):
        return cls.account_count
    
    def deposit(self, amount):
        if amount < 1:
            print("입금은 최소 1원 이상부터 가능합니다.")
            return
        self.balance += amount
        self.deposit_count += 1
        self.deposit_history.append(f"({dt.datetime.now()}){amount}원이 입금되었습니다.")
        if self.deposit_count % 5 == 0:
            interest = self.balance * 0.01
            self.balance += interest
            
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족합니다.")
            return 0
        self.balance -= amount
        self.withdraw_history.append(f"({dt.datetime.now()}){amount}원이 입금되었습니다.")
        return amount
    
    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.owner}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고: {self.balance:,}")
        
    def show_deposit_history(self):
        for val in self.deposit_history:
            print(val)
    
    def show_withdarw_history(self):
        for val in self.withdraw_history:
            print(val)

p = Account("파이썬", 100000000)

print("<271>")
        
# 272
# 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.
print("<272>")

# 273
# Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.
print("<273>")

# 274
# Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.
print("<274>")

# 275
# Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.
print("<275>")

# 276
# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.
print("<276>")
p.display_info()

# 277
# 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.
print("<277>")
print("")

# 278
# Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.
account_list = []

p = Account("파이썬", 100000001)
j = Account("자바", 200002)
js = Account("자바스크립트", 10000003)
c = Account("C언어", 10023)

account_list.append(p)
account_list.append(j)
account_list.append(js)
account_list.append(c)

print("<278>")
print(account_list)
    
# 279
# 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.
standard_amount = 1000000
print("<279>")
print("--------------------------")
for account in account_list:
    if account.balance >= standard_amount:
        account.display_info()
        print("--------------------------")
        
# 280
# 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.
print("<280>")