from Board import Board
from Controller import Controller
from Match import Match
from Agents import HumanAgent
from Agents import RandomAgent
from Agents import MinimaxAgent
from Heuristics import Heuristics
from OnlineMatch import OnlineMatch
from ConsoleManager import ConsoleManager
import os
import time
EMPTY=0
BLACK=1
WHITE=2
SELECT=3

# player1 = MinimaxAgent(BLACK,1,Heuristics().H4)
# # player1 = RandomAgent(WHITE)
# player2 = RandomAgent(WHITE)
# # player2 = MinimaxAgent(WHITE,1,Heuristics().H1)
# # player2 = MinimaxAgent(WHITE,1,Heuristics().H1)
# h=None
# bb=0
# N=100
# for i in range(N):
#     b,w=Match.newLocalGame(player1,player2,0)
#     if b > w:
#         bb+=1
#     print("",100*(i+1)/N,"%")
#     # time.sleep(0.1)
#     # exit(1)
#     # os.system('clear')
# print(bb/N)
#
player1 = None
player2 = None
h = None
# Match.newLocalGame(HumanAgent(BLACK),HumanAgent(WHITE))
# exit(1)
while(1):
    os.system('clear')
    print("Choose game type :")
    print("(1) Local game")
    print("(2) Online game")
    choice = int(input("Select : "))
    if choice == 1 :
        while 1:
            pass
            os.system('clear')
            print("LOCAL GAME")
            print("Choose First player's type :")
            player1 = ConsoleManager.askUserForPlayerType(BLACK)
            os.system('clear')
            print("LOCAL GAME")
            print("Choose Second player's type :")
            player2 = ConsoleManager.askUserForPlayerType(WHITE)

            b,w=Match.newLocalGame(player1,player2)
            if not int(input("Enter (1) to play again, (0) to exit")) :
                break
    elif choice == 2 :
        while(1):
            print("Choose an option:")
            print("(1) Join game")
            print("(2) New game")
            print("(0) go back")
            choice = int(input("Select : "))
            if choice == 1 :
                gameID = input("Enter the game ID :")
                print("Join the game as : ")
                player = ConsoleManager.askUserForPlayerType(WHITE)
                OnlineMatch.newOnlineGame(player,gameID)
            elif choice == 2 :
                OnlineMatch.newOnlineGame(ConsoleManager.askUserForPlayerType(BLACK))
            elif choice == 0 :
                break
            else :
                print("Invalid input")
    else :
        print("Invalid input")


# N=5
# black=0
# white=0
# for i in range(N) :
#     b,w=Match.newLocalGame(player1,player2)
#     print(i/N)
#
#     print("b :{}   w :{}".format(b,w))
#     time.sleep(0.5)
#     if b > w:
#         black+=1
#     else:
#         white+=1
# print("Black : {}%\nWhite : {}%".format(100*black/N,100*white/N))
