# lab25-ATM.py
#bank = {CN: "name", "balance}

class Bank:
    def __init__(self):
        self.bank = {}
        self.transactions = {}

    def __repr__(self):
        ret = ''
        return str(self.transactions) + str(self.bank)

    def new_client(self, CN, name, balance, ):
        self.bank[CN] = [name, balance]
        self.transactions[CN] = [f'starting balance {balance}']

    def check_balance(self, CN):
        return self.bank[CN][1]

    def deposit(self, CN, amount):
        self.bank[CN][1] += amount
        self.transactions[CN] += [f'deposit of {amount}']
        return f"Your just deposited ${amount}. Your balance is now ${self.check_balance(CN)}"

    def withdraw(self, CN, amount):
        if amount > self.bank[CN][1]:
            return f'sorry you only have {self.bank[CN][1]} in your account we can not give you {amount}.'
        else:
            self.bank[CN][1] -= amount
            self.transactions[CN] += [f'withdrawal of {amount}']
            return f"Your just withdrew ${amount}, your balance is now ${self.bank[CN][1]}"

    def print_transactions(self, CN):
        return self.transactions[CN]


BankofAmerica = Bank()
BankofAmerica.new_client(123456789, 'mitchell', 10000)
BankofAmerica.new_client(789456123, 'tyler', 8000)
BankofAmerica.new_client(100000000, "Santa", 1000000000)
BankofAmerica.deposit(123456789, 200)
BankofAmerica.withdraw(123456789, 80)
BankofAmerica.deposit(123456789, 2000)

requests = 0
card = 0
while requests > -1:
    if requests == 0:
        card = int(input("what is your card number"))
    print('\nOptionns: \ncheck balance: c \ndeposit: d\nwithdrawal: w\nfor a list of past transactions: t\nexit: e')
    to_do = input('what would you like to do >>  ')
    if to_do == "c":
        print(BankofAmerica.check_balance(card))
        requests += 1
    elif to_do == "d":
        cash = int(input('how much would you like to deposit today? >> '))
        print(BankofAmerica.deposit(card, cash))
        requests += 1
    elif to_do == 'w':
        cash = int(input("How much would you like to withdraw? >> "))
        print(BankofAmerica.withdraw(card, cash))
        requests += 1
    elif to_do == 't':
        print(BankofAmerica.transactions[card])
        requests += 1
    elif to_do == 'e':
        print("thank you for choosing Bank of America.")
        requests = -1






