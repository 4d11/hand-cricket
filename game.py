import argparse
from players import Human, RandomBot

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


def _initialize_game(args):
    print(args)
    player1 = Human('Player 1', args.n_wickets)
    if args.play2:
        player2 = Human('Player 2', args.n_wickets)
    else:
        player2 = RandomBot('PlayerBot 2', args.n_wickets)

    game = Game(player1, player2)
    return game

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cricket')
    parser.add_argument('--2player', dest="play2", action='store_true',
                        help="play with 2 human players")
    parser.add_argument('-w', '--wickets', dest="n_wickets", type=int,
                        default=2, help="the number of wickets")

    game = _initialize_game(parser.parse_args())
    game.play()
