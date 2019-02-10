class User:
    __username: str
    __messages: list

    def __init__(self, username):
        self.__username = username
        self.__messages = []

    def add_message(self, message):
        self.__messages.append(message)

    def get_messages(self):
        return self.__messages

    def print_message(self, order, num):
        if num < len(self.__messages):
            message = self.__messages[num]
            if order == 'first':
                print(f'{self.__username}: {message.get_content()}')
            else:
                print(f'{message.get_content()} :{self.__username}')


class Message:
    __content: str
    __sender: User

    def __init__(self, username, content):
        self.__username = username
        self.__content = content

    def get_content(self):
        return self.__content


users = {}
while True:
    data = input()

    if data == 'exit':
        chats = input()
        user1, user2 = chats.split()

        user1 = users[user1]
        user2 = users[user2]

        max_messages = max(len(user1.get_messages()), len(user2.get_messages()))

        if max_messages > 0:
            for i in range(0, max_messages):
                user1.print_message("first", i)
                user2.print_message("second", i)
        else:
            print("No messages")
        break

    command = data.split()[0]

    if command == 'register':
        username = data.split()[1]
        if not username in users:
            users[username] = User(username)
        pass
    else:
        sender = command
        recipient = data.split()[2]
        content = data.split()[3]

        if recipient in users and sender in users:
            users[sender].add_message(Message(recipient, content))
