class BankAccount:
    __name: str
    __bank: str
    __balance: float

    def __init__(self, bank, name, balance):
        self.set_name(name)
        self.set_bank(bank)
        self.set_balance(balance)

    def set_name(self, name):
        if not isinstance(name, str):
            raise Exception
        self.__name = name

    def set_bank(self, bank):
        if not isinstance(bank, str):
            raise Exception
        self.__bank = bank

    def set_balance(self, balance):
        if not isinstance(balance, float):
            raise Exception
        self.__balance = balance

    def get_name(self):
        return self.__name

    def get_bank(self):
        return self.__bank

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f'{self.__name} -> {self.__balance:.2f} ({self.__bank})'


bank_accounts = []
while True:
    data = input()
    if data == 'end':
        break

    bank, name, balance = data.split(' | ')
    bank_accounts.append(BankAccount(bank, name, float(balance)))

bank_accounts = sorted(bank_accounts, key=lambda b: (b.get_balance(), -len(b.get_bank())), reverse=True)


for acc in bank_accounts:
    print(acc)


