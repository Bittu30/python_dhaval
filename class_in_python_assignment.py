# This is assignment of classes tutorials

class Avengers:
    def __init__(self, name, age, gender, superpower, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.superpower = superpower
        self.weapon = weapon

    def get_superpower(self):
        pass

    def get_weapon(self):
        pass

    def get_gender(self):
        pass

    def __str__(self):
        return f'{self.name} {self.age},is the Avenger of having {self.superpower} and weapon as {self.weapon}'

    def __lt__(self, other):
        pass


captain_america = Avengers('Captain America', '35', 'Male', 'super strength','shield')
print(captain_america)
