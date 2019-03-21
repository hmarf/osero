class Player:

    def __init__(self, stone, name, education_bord):
        self.stone = stone
        self.name = name
        self.EVALUATION_BOARD = education_bord

    def play(self, board):
        availables = board.availables(self.stone)
        return self.think(board, availables)
