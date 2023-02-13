# this is class tutorial in python

import datetime


class CricketPlayer:
    def __init__(self, fname, lname, team, birthyear):
        self.first_name = fname
        self.last_name = lname
        self.team = team
        self.birth_year = birthyear
        self.scores = []

    def add_scores(self, scores):
        self.scores.append(scores)

    def get_average_scores(self):
        return sum(self.scores) / len(self.scores)

    def get_age(self):
        return datetime.datetime.now().year - self.birth_year

    def __str__(self):
        return f'{self.first_name}{self.last_name},is the cricketer of {self.team}'

    def __lt__(self, other):
        my_score = self.scores
        other_scores = other.scores
        return my_score > other_scores


virat = CricketPlayer('virat', 'kohli', 'india', 1988)
virat.add_scores(49)
virat.add_scores(89)
virat.add_scores(136)

print(virat)
print(virat.get_age())
print(virat.get_average_scores())

david = CricketPlayer('david', 'warner', 'Aus', 1990)
david.add_scores(39)
david.add_scores(56)
david.add_scores(92)

print(david)
print(david.get_age())
print(david.get_average_scores())

print(virat < david)






