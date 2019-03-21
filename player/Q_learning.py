import copy
import random

from .Player_Q import Player_Q
from .Quantity import Quantity

class Q_learning(Player_Q):
    
    def policy(self,board,availables):
        self.last_board = copy.deepcopy(board)
        if random.random() < (self.e/(self.action_count//10000+1)):
            move = random.choice(availables) #availables[random.randrange(len(availables))]
        else:
            qs = []
            for available in availables:
                qs.append(self.q.get(tuple(self.last_board.flatten_data()),available))
            max_q = max(qs)
            if qs.count(max_q) > 1:
                best_options = [i
                                for i in range(len(availables))
                                if qs[i] == max_q]
                i = random.choice(best_options)
            else:
                i = qs.index(max_q)
            move = availables[i]
        self.last_move = move
        x, y = move
        return x, y, self.stone

    def getGameResult(self,bord,opponent_player=None):
        bord_copy = copy.deepcopy(bord)

        opp_move = opponent_player.play(bord_copy)
        x, y, opp_stone = opp_move
        if not(x == y == opp_stone == 0):
            bord_copy.put(x,y,opp_stone)
        game_over = not(bord_copy.is_playable())

        reward = 0
        if game_over:
            winner = bord_copy.get_winner()
            if winner == self.stone:
                reward = 1
            elif winner == 0:
                reward = 0
            else:
                reward = -1

        if self.last_move != None:
            self.learn(self.last_board,self.last_move,reward,bord_copy,game_over)

        if not game_over:
            self.action_count += 1
            self.last_move = None
            self.last_board = None

    def learn(self,s,a,r,fs,game_over):
        board_data = s.flatten_data()
        _list = []
        for available in fs.availables(self.stone):
            _list.append(self.q.get(tuple(fs.flatten_data()),available))
        if game_over or len(_list) == 0:
            max_q_new = 0
        else:
            max_q_new = max(_list)
        self.q.update(tuple(board_data),a,r,max_q_new)


    def think(self,board,availables):
        if len(availables) == 0:
            return 0, 0, 0
        return self.policy(board,availables)

    def battleMode(self):
        self.e = 0

