class Birthday:
    __day: int
    __month: int
    __year: int

    def __init__(self, day, month=None, year=None):
        self.__day = day
        self.__month = month
        self.__year = year

    def set_day(self, day):
        self.__day = day

    def get_day(self):
        return self.__day

    def remove_day(self):
        return self.get_day() - 1

    def __str__(self):
        return f'My day is {self.__day}.{self.__month}.{self.__year}'


bdy1 = Birthday(day=1, month=12, year=1988)
print(bdy1)

data = input()
bdy2 = eval('Birthday(' + data + ')')
print(bdy2)

day, month, year = input().split(' ')
bdy3 = Birthday(day, month, year)

a = [1, 2, 3]
if isinstance(a, list):
    pass
