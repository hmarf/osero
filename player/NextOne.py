from .Player import Player
import copy

class NextOne(Player):

    def think(self,board,availables):
        if not availables:
            return "pass"
        bp = -10000
        for x, y in availables:
            board1 = copy.deepcopy(board)
            board1.put(x,y,self.stone)
            if bp < self.evaluate(board1,self.stone):
                bp = self.evaluate(board1,self.stone)
                x1 = x
                y1 = y
        return x1, y1, self.stone

    def evaluate(self,board1,stone):
        bp = 0
        for i in range(board1.SIZE):
            for j in range(board1.SIZE):
                if board1[i][j] == self.BLANK:
                    continue
                elif board1[i][j] == stone:
                        bp += self.EVALUATION_BOARD[i][j]
                else:
                        bp -= self.EVALUATION_BOARD[i][j]
        return bp

    
    def getGameResult(self,bord,opponent_player=None):
        pass