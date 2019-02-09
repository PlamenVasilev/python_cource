class Exercise:
    __topic: str
    __course_name: str
    __judge_contest_link: str
    __problems: list

    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.set_topic(topic)
        self.set_course_name(course_name)
        self.set_judge_contest_link(judge_contest_link)
        self.set_problems(problems)

    def set_topic(self, topic):
        if not isinstance(topic, str):
            raise Exception
        self.__topic = topic

    def set_course_name(self, course_name):
        if not isinstance(course_name, str):
            raise Exception
        self.__course_name = course_name

    def set_judge_contest_link(self, judge_contest_link):
        if not isinstance(judge_contest_link, str):
            raise Exception
        self.__judge_contest_link = judge_contest_link

    def set_problems(self, problems):
        if not isinstance(problems, list):
            raise Exception
        self.__problems = problems

    def print(self):
        print(f'Exercises: {self.__topic}')
        print(f'Problems for exercises and homework for the "{self.__course_name}" course @ SoftUni.')
        print(f'Check your solutions here: {self.__judge_contest_link}')
        for p in range(0,len(self.__problems)):
            print(f'{p+1}. {self.__problems[p]}')


exercises = []
while True:
    data = input()
    if data == "go go go":
        break
    else:
        topic, name, link, problems = data.split(' -> ')
        exercises.append(Exercise(topic, name, link, problems.split(', ')))

for ex in exercises:
    ex.print()



