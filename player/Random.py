import random
from .Player import Player

class Random(Player):

    def think(self,board,availables):
        if not availables:
            return 0, 0, 0
        x, y = availables[random.randint(0,len(availables)-1)]
        return x, y, self.stone

    
    def getGameResult(self,bord,opponent_player=None):
        pass