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
        """ Make the move
        :return: int [0,6]
        """
        pass

    @abstractmethod
    def track(self, move):
        """ Get the opposite players move
        :return: None
        """
        pass


class Human(Player):
    def track(self, move):
        pass

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
    def track(self, move):
        pass

    def play(self):
        n = random.randint(0,6)
        print("{}'s move: {}".format(self.name, n))
        return n


class SmartBot(Player):
    def __init__(self, name, n_wickets):
        super().__init__(name,n_wickets)
        self.tracker = {0:1,1:1,2:1,3:1,4:1,5:1,6:1}
        self.probs = {0:1/7, 1:1/7, 2:1/7, 3:1/7, 4:1/7, 5:1/7, 6:1/7}
        self.total = 7
        self.is_random = False

    def track(self, move):
        self.tracker[move] += 1
        self.total += 1

    def _get_relative_probs(self):
        return {x:self.tracker[x]/self.total for x in self.tracker.keys()}

    def play(self):
        print(self.tracker, self.total)
        rel_probs = self._get_relative_probs()
        most_likely = max(rel_probs, key=lambda k: rel_probs[k])
        print("{}'s move: {}".format(self.name, most_likely))
        return most_likely

