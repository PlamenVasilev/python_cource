from abc import ABC, abstractmethod


class BaseMonster(ABC):
    __name: str
    __id: int
    __strength: int
    __ugliness: int

    @abstractmethod
    def __init__(self, name, mid, strength, ugliness):
        self.set_name(name)
        self.set_id(mid)
        self.set_strength(strength)
        self.set_strength(ugliness)

    def set_name(self, name):
        if not isinstance(name, str):
            raise Exception('Name must be string')
        self.__name = name

    def get_name(self):
        return self.__name

    def set_id(self, mid):
        if not isinstance(mid, int):
            raise Exception('Id must be integer')
        self.__id = mid

    def get_id(self):
        return self.__id

    def set_strength(self, strength):
        if not isinstance(strength, int):
            raise Exception('Strength must be integer')
        self.__strength = strength

    def get_strength(self):
        return self.__strength

    def set_ugliness(self, ugliness):
        if not isinstance(ugliness, int):
            raise Exception('Ugliness must be integer')
        self.__ugliness = ugliness

    def get_ugliness(self):
        return self.__ugliness


class Hydralisk(BaseMonster):
    __range: str

    def __init__(self, name, mid, strength, ugliness, range):
        super().__init__(name, mid, strength, ugliness)
        self.set_range(range)

    def set_range(self, range):
        if not isinstance(range, str):
            raise Exception('Range must be string')
        self.__range = range

    def get_range(self):
        return self.__range


class Zergling(BaseMonster):
    __speed: int

    def __init__(self, name, mid, strength, ugliness, speed):
        super().__init__(name, mid, strength, ugliness)
        self.set_speed(speed)

    def set_speed(self, speed):
        if not isinstance(speed, int):
            raise Exception('Speed must be integer')
        self.__speed = speed

    def get_speed(self):
        return self.__speed


listmons_army = []

while True:
    data = input()

    if data == 'stopAddingArmy':
        break

    try:
        monster = eval(data)
        listmons_army.append(monster)
    except Exception as e:
        print(str(e))

speed = sum([m.get_speed() for m in listmons_army if isinstance(m, Zergling)])
strength = sum([m.get_strength() for m in listmons_army])
hydralisks = sum([1 for m in listmons_army if isinstance(m, Hydralisk)])
zerglings = sum([1 for m in listmons_army if isinstance(m, Zergling)])



print(f'Overall speed of army: {speed}')
print(f'Overall stength: {strength}')
print(f'Hydralisk: {hydralisks}; Zergling: {zerglings}')
