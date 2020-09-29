class User:
    def __init__(self, name_parameter):
        self.name = name_parameter
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f" User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


instance1 = User('lingX')
instance2 = User('shuZ')
instance3 = User('leeJ')

instance1.make_deposit(1000).make_deposit(1000).make_deposit(1000).make_withdrawal(200)

instance2.make_deposit(1000).make_deposit(1000).make_deposit(1000).make_withdrawal(200)

instance3.make_deposit(1000).make_deposit(1000).make_deposit(1000).make_withdrawal(200)

instance1.display_user_balance()
instance2.display_user_balance()
instance3.display_user_balance()

instance2.make_deposit(100).make_deposit(100).make_withdrawal(500).make_withdrawal(500).display_user_balance()

instance3.make_deposit(10000).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200).display_user_balance()

instance1.transfer_money(instance2,1000)
instance1.display_user_balance()
instance2.display_user_balance()
