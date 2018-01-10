from abc import abstractmethod
from abc import ABCMeta
import random

class Player:
    __metaclass__ = ABCMeta

    def __init__(self, name, n_wickets):
        self.score = 0
        self.wickets = n_wickets
        self.name = name

    @abstractmethod
    def play(self):
        pass


class Human(Player):
    def play(self):
        n = input("{}'s move: ".format(self.name))
        try:
            n = int(n)
            if not 0 <= n <=6:
                raise ValueError
        except ValueError:
            print("Please input a valid number")
        return n


class RandomBot(Player):
    def play(self):
        n = random.randint(0,6)
        print("{}'s move: {}".format(self.name, n))
        return n
