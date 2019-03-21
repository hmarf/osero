import random
import copy
from .Player import Player

class CountStone(Player):

    def think(self,board,availables):
        if not availables:
            return 0, 0, 0
        board1 = copy.deepcopy(board)
        max_count = 0
        count = 0
        for x, y in availables:
            board1 = copy.deepcopy(board)
            board1.put(x,y,self.stone)
            for i in range(board1.SIZE):
                for j in range(board1.SIZE):
                    if board1[i][j] == self.stone:
                        count += 1
                if count > max_count:
                    x1 = x
                    y1 = y
        return x1, y1, self.stone

    def getGameResult(self,bord,opponent_player=None):
        pass