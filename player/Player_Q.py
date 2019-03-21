from .Quantity import Quantity

class Player_Q:
    def __init__(self, stone, name, filename):
        self.stone = stone
        self.name = name        
        self.alpha = 0.3
        self.gamma=0.9
        print(filename)
        self.q = Quantity(self.alpha,self.gamma,filename)
        self.next_q_list = []
        self.e = 0.2
        self.action_count = 0
        self.last_move=None
        self.last_board=None

    def play(self, board):
        availables = board.availables(self.stone)
        return self.think(board, availables)