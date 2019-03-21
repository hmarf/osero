from Othello import Othello
from Stone import Stone
from player.Q_learning import Q_learning
from player.NextOne import NextOne
from player.CountStone import CountStone
from player.Random import Random
from player.Naive import Naive
from player.MLP import MLP_p

def get_player(mode,name,color,education_bord=None):

    if color == 'black':
        if mode == 'NextOne':
            player =NextOne(Stone("●"),name,education_bord)
        elif mode == 'CountStone':
            player = CountStone(Stone("●"),name,education_bord)
        elif mode == 'Random':
            player = Random(Stone("●"),name,education_bord)
        elif mode == 'Q_learning':
            player = Q_learning(Stone("●"),name,education_bord)
        elif mode == 'Naive':
            player = Naive(Stone("●"),name,education_bord)
        elif mode == 'MLP':
            player = MLP_p(Stone("●"),name,education_bord)
    else:
        if mode == 'NextOne':
            player = NextOne(Stone("○"),name,education_bord)
        elif mode == 'CountStone':
            player = CountStone(Stone("○"),name,education_bord)
        elif mode == 'Random':
            player = Random(Stone("○"),name,education_bord)
        elif mode == 'Q_learning':
            player = Q_learning(Stone("○"),name,education_bord)
        elif mode == 'Naive':
            player = Naive(Stone("○"),name,education_bord)
        elif mode == 'MLP':
            player = MLP_p(Stone("○"),name,education_bord)
    return player

player1 = get_player('MLP','P1','black')
player2 = get_player('Random','P2','white')
player1.battleMode()
game = Othello(nplay=600,show_result=True,show_board=False)
game.play(player1,player2)
# player2 = get_player('Q_learning','P2','white','no')
# game = Othello(nplay=120000,show_result=True,show_board=False)
# game.play(player1,player2)

# player1.q.save('p1.pickle')
# player2.q.save('p2.pickle')
# player1.battleMode()
# print()

# player2 = get_player('Random','P2','white')
# game = Othello(nplay=600,show_result=True,show_board=False)
# game.play(player1,player2)