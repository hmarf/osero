from .Player import Player

class User(Player):

    def think(self, board, availables):
        if not availables:
            return 0, 0, 0
        while True:
            try:
                line = input("Y X or quit: ")
            except:
                exit(1)
            if line == "quit" or line == "exit":
                exit(1)
            try:
                x, y = map(int, line.split())
                if (x, y) in availables:
                    board.put(x, y, self.stone)
                    return x, y
                else:
                    print("そこには置けません")
            except:
                print("意味不明")