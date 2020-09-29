class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = 0.01
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print('Insufficient funds: Charging a $5 fee')
        self.balance -= 5
        return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1+self.int_rate)
        return self
    
account1 = BankAccount(0.01, 0)
account2 = BankAccount(0.05, 10000)

account1.deposit(500).deposit(100).deposit(500).withdraw(1000).yield_interest().display_account_info()
account2.deposit(500).deposit(100).withdraw(1000).withdraw(1000).withdraw(1000).withdraw(1000).yield_interest().display_account_info()
    
