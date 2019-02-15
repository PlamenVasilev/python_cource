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
        for technique in sorted(self.__techniques, key= lambda k: (-self.__techniques[k], k)):
            prnt += f'\n- {technique} <!> {self.__techniques[technique]}'

        return prnt

    def get_techniques(self):
        return list(self.__techniques)

    def get_technique(self, tech):
        if tech in self.__techniques:
            return self.__techniques[tech]
        else:
            pass


gladiators = {}
while True:
    data = input()
    if data == 'Ave Cesar':
        break

    if data.find('->')>=0:
        name = data.split(' -> ')[0]
        technique = data.split(' -> ')[1]
        skill = int(data.split(' -> ')[2])

        if name in gladiators:
            gladiators[name].set_skill(technique, skill)
        else:
            gladiator = Gladiator(name)
            gladiator.set_skill(technique, skill)
            gladiators[name] = gladiator
    else:
        try:
            gladiator_1 = data.split(' vs ')[0]
            gladiator_2 = data.split(' vs ')[1]
            if gladiator_1 in gladiators and gladiator_2 in gladiators:
                common_techniques = list(set(gladiators[gladiator_1].get_techniques()) & set(gladiators[gladiator_2].get_techniques()))
                if len(common_techniques):
                    for tech in common_techniques:
                        if gladiators[gladiator_1].get_technique(tech) > gladiators[gladiator_2].get_technique(tech):
                            del gladiators[gladiator_2]
                        elif gladiators[gladiator_1].get_technique(tech) < gladiators[gladiator_2].get_technique(tech):
                            del gladiators[gladiator_1]
                        else:
                            pass
        except:
            pass

gladiators = {k: v for k, v in sorted(gladiators.items(), key=lambda kv: kv[1].get_total_skill(), reverse=True)}
for name, gladiator in gladiators.items():
    print(gladiator)
