from Board import Board
from Stone import Stone

class Othello:

    def __init__(self,nplay=1,show_result=False,show_board=False):

        self._nplay = nplay
        self._show_result = show_result
        self._show_board = show_board
        self._p1_win_count = 0
        self._p2_win_count = 0
        self._draw_count = 0
        self.BLACK = Stone("●")
        self.WHITE = Stone("○")
        self.BLANK = Stone("×")
        self.OPPONENT = {self.BLACK: self.WHITE, self.WHITE: self.BLACK}

    def play(self,player1,player2):
        p1 = player1
        p2 = player2
        for i in range(self._nplay):
            board = Board()
            while board.is_playable():
                x, y , stone = p1.play(board)
                if not( x == y == stone == 0):
                    count = 0
                    board.put(x,y,stone)
                # else:
                #     count += 1
                #     if count > 1:
                #         break
                p1.getGameResult(board,opponent_player=p2)
                (p1, p2) = (p2,p1)
            self.count_result(board)
            if self._show_result:
                self.show_result(str(i))
        return self._p1_win_count, self._p2_win_count, self._draw_count

    # 遺伝的アルゴリズムの時の show_result
    # def show_result(self, board):
    #     computer_stones = board.count(BLACK)
    #     user_stones = board.count(WHITE)
    #     if computer_stones > user_stones:
    #         return 8, 1
    #     elif computer_stones < user_stones:
    #         return 1, 8
    #     else:
    #         return 3, 3

    # q-learning の時の show_result

    def count_result(self, board):
        player1_stones = board.count(self.BLACK)
        player2_stones = board.count(self.WHITE)
        if player1_stones > player2_stones:
            self._p1_win_count += 1
        elif player1_stones < player2_stones:
            self._p2_win_count += 1
        else:
            self._draw_count += 1

    def show_result(self,count):
        print(count+') Player1: '+str(self._p1_win_count)+'  Player2: '+str(self._p2_win_count)+'  Draw: '+str(self._draw_count))