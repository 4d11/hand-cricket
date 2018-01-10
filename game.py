
class Game:
    def __init__(self, batter, bowler):
        self.batter = batter
        self.bowler = bowler

    def __str__(self):
        s = """
        {0} is batting and {1} is bowling. 
        {0} is {2} with {3} wickets left
        {1} is {4} with {5} wickets left
        """.format(self.batter.name,self.bowler.name,
                   self.batter.score, self.batter.wickets,
                   self.bowler.score, self.bowler.wickets
        )
        return s

    def play(self):
        while True:
            print(self)
            bat = self.batter.play()
            bowl = self.bowler.play()
            if bowl == bat:
                print("out")
                self.batter.wickets -= 1
                if self.batter.wickets == 0:
                    if self.bowler.wickets == 0:
                        if self.bowler.score == self.batter.score:
                            print("TIE!")
                        else:
                            print("{} wins !".format(self.bowler.name))
                        exit()
                    else:
                        self.batter, self.bowler = self.bowler, game.batter
            elif bat == 0:
                self.batter.score += bowl
            else:
                self.batter.score += bat
            if self.batter.score > self.bowler.score and self.bowler.wickets == 0:
                print("{} wins !".format(self.batter.name))
                exit()


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
            return n
        except ValueError:
            print("Please input a valid number")
            return self.play()



def _initialize_game():
    player1 = Player('Player1')
    player2 = Player('Player2')
    game = Game(player1, player2)
    return game


def game():
    game = _initialize_game()
    while True:
        print(game)
        bowl = game.bowler.play()
        bat = game.batter.play()
        if bowl == bat:
            print("out")
            game.batter.wickets -= 1
            if game.batter.wickets == 0:
                if game.bowler.wickets == 0:
                    if game.bowler.score == game.batter.score:
                        print("TIE!")
                    else:
                        print("{} wins !".format(game.bowler.name))
                    exit()
                else:
                    game.batter, game.bowler = game.bowler, game.batter
        elif bat == 0:
            game.batter.score += bowl
        else:
            game.batter.score += bat
        if game.batter.score > game.bowler.score and game.bowler.wickets == 0:
            print("{} wins !".format(game.batter.name))
            exit()

if __name__ == '__main__':
    game = _initialize_game()
    game.play()