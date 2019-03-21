from .Player import Player

class Naive(Player):

	def think(self,board,availables):
		if len(availables) == 0:
			return 0, 0, 0
		for i in range(0,8):
			for j in range(0,8):
				if (i,j) in availables:
					return i, j, self.stone

	def getGameResult(self,bord,opponent_player=None):
		pass