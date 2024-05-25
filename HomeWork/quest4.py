#Quest 4

class BankAccount:
    def __init__(self, acc_num, acc_holder):
        self.acc_num = acc_num
        self.acc_holder = acc_holder
        self.acc_balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.acc_balance += amount
            print(f"Deposited: ${amount:.2f}. Current balance: ${self.acc_balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.acc_balance:
            self.acc_balance -= amount
            print(f"Withdrew: ${amount:.2f}. Current balance: ${self.acc_balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.acc_balance

class SavingsAccount(BankAccount):
    def __init__(self, acc_num, acc_holder, interest_rate):
        super().__init__(acc_num, acc_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.acc_balance * self.interest_rate / 100
        self.acc_balance += interest
        print(f"Interest applied: ${interest:.2f}. New balance: ${self.acc_balance:.2f}")

    def __str__(self):
        return f"Current balance: ${self.acc_balance:.2f}, Interest rate: {self.interest_rate}%"

def main():
    my_account = BankAccount("793893", "Alaa Tawil")
    my_account.deposit(900) 
    my_account.withdraw(700) 
    print(f"Balance after withdrawal: ${my_account.get_balance():.2f}")

    my_savings = SavingsAccount("793893", "Alaa Tawil", 6.9)
    my_savings.deposit(1000)  
    my_savings.apply_interest()  
    print(my_savings)

if __name__ == "__main__":
    main()
