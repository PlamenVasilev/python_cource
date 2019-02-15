class Gladiator:
    __name: str
    __techniques: dict
    __total_skill: int

    def __init__(self, name: str):
        self.__name = name
        self.__techniques = {}
        self.__total_skill = 0

    def get_name(self):
        return self.__name

    def get_total_skill(self):
        return self.__total_skill

    def set_skill(self, technique: str, skill: int):
        if technique in self.__techniques:
            if self.__techniques[technique]< skill:
                self.__total_skill -= self.__techniques[technique]
                self.__total_skill += skill
                self.__techniques[technique] = skill
        else:
            self.__techniques[technique] = skill
            self.__total_skill += skill

    def __str__(self):
        prnt = f'{self.get_name()}: {self.get_total_skill()} skill'
        for technique in sorted(self.__techniques.keys(), reverse=True):
            prnt += f'\n- {technique} <!> {self.__techniques[technique]}'

        return prnt


gladiators = {}
while True:
    data = input()
    if data == 'Ave Cesar':
        break
    
    name = data.split(' -> ')[0]
    technique = data.split(' -> ')[1]
    skill = int(data.split(' -> ')[2])
    
    if name in gladiators:
        gladiators[name].set_skill(technique, skill)
    else:
        gladiator = Gladiator(name)
        gladiator.set_skill(technique, skill)
        gladiators[name] = gladiator

gladiators = {k: v for k, v in sorted(gladiators.items(), key=lambda kv: kv[1].get_total_skill(), reverse=True)}
for name, gladiator in gladiators.items():
    print(gladiator)
