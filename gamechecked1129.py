import random

moves = ['rock', 'paper', 'scissors']

class Player:
    my_move = None
    their_move = None
    
    def move(self):
        return 'rock'
    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move
            
    def learn (self, my_move,their_move):
        self.their_move = their_move 

class RockerPlayer(Player):
    pass 
    
class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'
            
    def learn(self,my_move,their_move):
        self.my_move = my_move

class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock,Paper,Scissors?").lower()
            if move in moves:
                return move
            print("Invalid Choice.Try again").lower()
            
def beats(one, two): 
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))
    
class Game():
    p1_score = 0
    p2_score = 0
        
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2    
        
            
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p2.learn(move1,move2)
        self.p2.learn(move2,move1)
        print(f"Player 1: {move1}")
        print(f"Player 2: {move2}")
        if beats(move1, move2):
            self.p1_score += 1
            print("Player 1 won!")
        elif beats(move2, move1):
            self.p2_score += 1
            print("Player 2 won!")
        else:
            print("Tie!!!")
        print("Scores: ")
        print(f"Player 1: {self.p1_score}")
        print(f"Player 2:s {self.p2_score}")
    
    def play_game(self):
        print("Game start!")
        for round in [1, 2, 3]:
            print(f"Round{round}:")
            self.play_round()
        print("Scores:")
        print(f"Player 1: {self.p1_score}")
        print(f"Player 2: {self.p2_score}")
        if self.p1_score < self.p2_score:
            print("Player 2 won ")
        elif self.p1_score > self.p2_score:
            print("Player 1 won")
        else:
            print("TIE")
        print("Game over")
if __name__ == '__main__':
    Players = [
        RockerPlayer(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(Players)
    print(f"Human vs {p2.__class__.__name__}")
    game = Game(p1, p2)
    game.play_game()