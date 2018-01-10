class Player:
    def __init__(self, name):
        self.score = 0
        self.wickets = 2
        self.name = name


    def play(self):
        n = input("{}'s move: ".format(self.name))
        try:
            n = int(n)
            if not 0 <= n <=6:
                raise ValueError
        except ValueError:
            print("Please input a valid number")
        return n

