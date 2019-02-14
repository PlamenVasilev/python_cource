class Book:
    __title: str
    __author: str
    __price: float
    __chapters: list

    def __init__(self, title, author, price, chapters):
        self.__title = title
        self.__author = author
        self.__price = float(price)
        self.__chapters = chapters

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def get_chapters_num(self):
        return len(self.__chapters)


on_work = False
books = {}
sold_books = []
while True:
    data = input()
    if data == 'end work':
        if len(sold_books):
            sold_sum = 0.00
            for book in sold_books:
                print(f'SOLD: {book.get_title()} with author {book.get_author()}. Chapters in the book {book.get_chapters_num()}')
                sold_sum += book.get_price()

            print(f'Money: {sold_sum:.2f}')
        else:
            print('Bad day :(')
        break

    if data == 'on work':
        on_work = True
        continue

    if on_work:
        title = data.split()[0]
        if title in books:
            sold_books.append(books[title])
        else:
            print("No such book here")
    else:
        f_part, s_part = data.split(' -> ')

        title = f_part.split(' ')[0]
        author = f_part.split(' ')[1]
        price = f_part.split(' ')[2]
        chapters = s_part.split(',')

        if title and author and float(price) >= 0.01:
            if title not in books:
                books[title] = Book(title, author, price, chapters)

