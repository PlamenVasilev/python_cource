class Animal:
    __name: str
    __age: int

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise Exception
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age: int):
        if not isinstance(age, int):
            raise Exception
        self.__age = age

    def get_age(self):
        return self.__age

    def __init__(self, name: str, age: int):
        self.set_name(name)
        self.set_age(age)


class Dog(Animal):
    __number_of_legs: int

    def set_number_of_legs(self, num: int):
        if not isinstance(num, int):
            raise Exception
        self.__number_of_legs = num

    def get_number_of_legs(self):
        return self.__number_of_legs

    def __init__(self, name: str, age: int, legs: int):
        super().__init__(name, age)
        self.set_number_of_legs(legs)

    def produce_sound(self):
        print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")

    def get_priority(self):
        return 1

    def __str__(self):
        return f'Dog: {self.get_name()}, Age: {self.get_age()}, Number Of Legs: {self.get_number_of_legs()}'


class Cat(Animal):
    __intelligence_quotient: int

    def set_intelligence_quotient(self, quotient: int):
        if not isinstance(quotient, int):
            raise Exception
        self.__intelligence_quotient = quotient

    def get_intelligence_quotient(self):
        return self.__intelligence_quotient

    def __init__(self, name: str, age: int, quotient: int):
        super().__init__(name, age)
        self.set_intelligence_quotient(quotient)

    def produce_sound(self):
        print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")

    def get_priority(self):
        return 2

    def __str__(self):
        return f'Cat: {self.get_name()}, Age: {self.get_age()}, IQ: {self.get_intelligence_quotient()}'


class Snake(Animal):
    __cruelty_coefficient: int

    def set_cruelty_coefficient(self, quotient: int):
        if not isinstance(quotient, int):
            raise Exception
        self.__cruelty_coefficient = quotient

    def get_cruelty_coefficient(self):
        return self.__cruelty_coefficient

    def __init__(self, name: str, age: int, quotient: int):
        super().__init__(name, age)
        self.set_cruelty_coefficient(quotient)

    def produce_sound(self):
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")

    def get_priority(self):
        return 3

    def __str__(self):
        return f'Snake: {self.get_name()}, Age: {self.get_age()}, Cruelty: {self.get_cruelty_coefficient()}'


animals_collection = {}
while True:
    data = input()
    if data == "I'm your Huckleberry":
        animals_collection = {k: v for k, v in sorted(animals_collection.items(), key=lambda kv: kv[1].get_priority())}

        for name, animal in animals_collection.items():
            print(animal)
        break

    first = data.split()[0]

    if first == 'talk':
        name = data.split()[1]
        if name in animals_collection:
            animals_collection[name].produce_sound()
    else:
        name = data.split()[1]
        p1 = int(data.split()[2])
        p2 = int(data.split()[3])

        if first == 'Dog':
            animals_collection[name] = Dog(name, p1, p2)
        elif first == 'Cat':
            animals_collection[name] = Cat(name, p1, p2)
        elif first == 'Snake':
            animals_collection[name] = Snake(name, p1, p2)
