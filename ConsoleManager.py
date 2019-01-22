from Board import Board
from Controller import Controller
from Match import Match
from Agents import HumanAgent
from Agents import RandomAgent
from Agents import MinimaxAgent
from Heuristics import Heuristics
from OnlineMatch import OnlineMatch
import os
import time


class ConsoleManager:
    @classmethod
    def askUserForPlayerType(cls,diceColor):
        while(1):
            print("(1) Human Agent")
            print("(2) Random Agent")
            print("(3) Minimax Agent")
            print("(0) go back")
            choice = int(input("Select : "))
            if choice == 1 :
                player = HumanAgent(diceColor)
                break
            elif choice == 2 :
                player = RandomAgent(diceColor)
                break
            elif choice == 3 :
                while(1):
                    os.system('clear')
                    print("Choose Heuristic :")
                    print("(1) Maximize own dice count [GREEDY]")
                    print("(2) Minimize own dice count [for fun]")
                    print("(3) Minimize opponents available actions")
                    print("(4) Special heuristic")
                    print("(0) go back")
                    choice = int(input("Select : "))
                    if choice == 1 :
                        h = Heuristics().H1
                        depth = int(input("Enter the maxDepth of the tree [ 1 suggested ] :"))
                        player = MinimaxAgent(diceColor,depth,h)
                        break
                    elif choice == 2 :
                        h = Heuristics().H2
                        depth = int(input("Enter the maxDepth of the tree :"))
                        player = MinimaxAgent(diceColor,depth,h)
                        break
                    elif choice == 3 :
                        h = Heuristics().H3
                        depth = int(input("Enter the maxDepth of the tree :"))
                        player = MinimaxAgent(diceColor,depth,h)
                        break
                    elif choice == 4 :
                        h = Heuristics().H4
                        depth = int(input("Enter the maxDepth of the tree [>3 suggested] :"))
                        player = MinimaxAgent(diceColor,depth,h)
                        break
                    elif choice == 0 :
                        break
                    else :
                        print("Invalid input")
                break
            elif choice == 0 :
                break
            else :
                print("Invalid input")
        print(player.type)
        return player
