class Website:
    __host: str
    __domain: str
    __queries: list

    def __init__(self, host: str, domain: str, queries: list = []):
        self.__host = host
        self.__domain = domain
        self.__queries = queries

    def __str__(self):
        if len(self.__queries)>0:
            return f'https://www.{self.__host}.{self.__domain}/query?={"&".join("["+el+"]" for el in self.__queries)}'
        else:
            return f'https://www.{self.__host}.{self.__domain}'

sites = []
while True:
    data = input()

    if data == 'end':
        for site in sites:
            print(site)
        break

    input_list = data.split(' | ')
    host = input_list[0]
    domain = input_list[1]
    queries = []
    if len(input_list) == 3:
        queries = input_list[2].split(',')

    sites.append(Website(host, domain, queries))

