class User:
    __username: str
    __messages: dict

    def __init__(self, username):
        self.__username = username
        self.__messages = {}

    def add_message(self, username, message):
        if not username in self.__messages:
            self.__messages[username] = []
        self.__messages[username].append(message)

    def get_messages(self, username):
        if username in self.__messages:
            return self.__messages[username]
        else:
            return []

    def print_message(self, username, order, num):
        messages = self.get_messages(username)
        if num < len(messages):
            message = messages[num]
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
        username1, username2 = chats.split()

        user1 = users[username1]
        user2 = users[username2]

        max_messages = max(len(user1.get_messages(username2)), len(user2.get_messages(username1)))

        if max_messages > 0:
            for i in range(0, max_messages):
                user1.print_message(username2, "first", i)
                user2.print_message(username1, "second", i)
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
            users[sender].add_message(recipient, Message(recipient, content))
