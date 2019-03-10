def get_id(first_name, last_name):
    return f'{first_name} {last_name}'


def card_valid(number):
    total = sum(list(map(int, number)))
    if total % 7 :
        return False
    else:
        return True


class Card:

    __number: str
    __id: str

    def __init__(self, first_name, last_name, number):
        self.__number = number
        self.__id = get_id(first_name, last_name)

    def get_number(self):
        return self.__number

    def get_id(self):
        return self.__id


class Person:

    __first: str
    __last: str
    __cards: dict
    __tickets: list
    __total: float

    def __init__(self, first_name, last_name):
        self.__first = first_name
        self.__last = last_name
        self.__cards = {}
        self.__tickets = []
        self.__total = 0

    def add_card(self, card):
        self.__cards[card.get_number()] = card

    def get_cards(self):
        return self.__cards

    def get_card(self, card_number):
        return self.__cards[card_number]

    def add_ticket(self, ticket):
        self.__tickets.append(ticket)
        self.__total += ticket.get_price()

    def get_name(self):
        return f'{self.__first} {self.__last}'

    def get_tickets(self):
        return self.__tickets

    def get_total(self):
        return self.__total


class Ticket:
    __destination: str
    __price: float
    __card: Card
    __person: Person

    def __init__(self, destination:str, person: Person, card: Card = None):
        self.__destination = destination
        self.__person = person
        self.__card = card
        self.__price = 0

        person.add_ticket(self)

    def get_price(self):
        price = sum(list(map(ord, self.__destination)))/100
        if self.__card:
            return price/2
        else:
            return price

    def get_discount(self):
        pass

    def __str__(self):
        if self.__card:
            return f'--{self.__destination}: {self.get_price():.2f}lv (using card {self.__card.get_number()})'
        else:
            return f'--{self.__destination}: {self.get_price():.2f}lv'


cards_number = int(input())

persons = {}
cards = {}
tickets = []
for _ in range(cards_number):
    first, last, number = input().split()

    person = Person(first, last)
    card = Card(first, last, number)
    person.add_card(card)

    persons[get_id(first, last)] = person
    cards[number] = card


while True:
    data = input()

    if data == 'time to leave!':
        break

    create, first_name, last_name, destination, card_number = data.split()
    id = get_id(first_name, last_name)
    #print(f'---------{first_name} {last_name} {card_number}')
    if card_valid(card_number):
        if card_number not in cards:
            card = Card(first_name, last_name, card_number)
            cards[card_number] = card
            print(f'issuing card {card_number}')

        if id in persons and card_number in persons[id].get_cards():
            ticket = Ticket(destination, persons[id], persons[id].get_card(card_number))
            tickets.append(ticket)
        elif cards[card_number].get_id() != id:
            print(f'card {card_number} already exists for another passenger!')
            person = Person(first_name, last_name)
            persons[get_id(first_name, last_name)] = person
            ticket = Ticket(destination, person)
            tickets.append(ticket)
        elif id in persons and card_number in cards:
            persons[id].add_card(cards[card_number])
            ticket = Ticket(destination, persons[id], cards[card_number])
            tickets.append(ticket)
        else:
            person = Person(first_name, last_name)
            persons[get_id(first_name, last_name)] = person
            ticket = Ticket(destination, person, cards[card_number])
            tickets.append(ticket)
    else:
        print(f'card {card_number} is not valid!')

        if id in persons:
            ticket = Ticket(destination, persons[id])
            tickets.append(ticket)
        else:
            person = Person(first_name, last_name)
            persons[get_id(first_name, last_name)] = person
            ticket = Ticket(destination, person)
            tickets.append(ticket)


for person in sorted(persons.values(), key=lambda p: -p.get_total()):
    if person.get_total():
        print(f'{person.get_name()}:')
        total_tickets = 0
        for ticket in sorted(person.get_tickets(), key=lambda t: -t.get_price()):
            print(ticket)
        print(f'total: {person.get_total():.2f}lv')
