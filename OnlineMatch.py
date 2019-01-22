from State import State
from Controller import Controller
from Board import Board
import os
import time
EMPTY=0
BLACK=1
WHITE=2
SELECT=3

class OnlineMatch:
    def __init__(self,turn,player,board,controller):
        self.player=player
        self.board=board
        self.turn=turn
        self.controller=controller
        self.result=0
        self.state=State(self.controller,board,player.diceColor,None)


    def finished(self):
        whiteNum,blackNum,emptyNum=self.controller.analyzeBoard(self.board.array)
        return emptyNum==0 or whiteNum == 0 or blackNum == 0

    def showResults(self,flag=0):
        w,b,e=self.controller.analyzeBoard(self.board.array)
        print("White : {}\nBlack : {}".format(w,b))
        if flag :
            if w > b:
                print("White wins")
            elif w < b :
                print("Black wins")
            else :
                print("Tie ! ")


    def printBoard(self,turn=None):
        if not turn :
            actions = self.controller.getActions(self.board.array,self.player.diceColor)
        else :
            actions = self.controller.getActions(self.board.array,turn)
        for act in actions:
            self.board.change(act[0],act[1],SELECT)
        print(self.board)
        self.board.clearSelections()

    def playOnline(self,gameID,flag=0):
        import time
        if not flag :
            active,self.turn,self.board = Board.fromURL(gameID)
            self.state.board = self.board
            os.system('clear')
            self.printBoard(self.turn)
            if active :
                if(self.turn == self.player.diceColor):
                    os.system('clear')
                    self.printBoard(self.turn)
                    if self.controller.getActions(self.board.array,self.player.diceColor):
                        action = self.player.getAction(self)
                        while not self.controller.validAction(self.board.array,self.player.diceColor,action):
                            print("Invalid Move, try again")
                            print(action)
                            action = self.player.getAction(self)
                        self.state = self.controller.performAction(self.state,action)
                        self.board = self.state.board
                        opponent = BLACK if self.player.diceColor == WHITE else WHITE
                        os.system('clear')
                        print(self.board)
                        Board.putBoard(True,self.board,opponent,gameID)
                        return 0

                    else :
                        print("No valid moves : PASS")
                        opponent = BLACK if self.player.diceColor == WHITE else WHITE
                        os.system('clear')
                        print(self.board)
                        Board.putBoard(True,self.board,opponent,gameID)
                        return -1
                else :
                    print("Waiting for opponent's turn")
                    time.sleep(1)
                    return self.playOnline(gameID)
            else :
                print("Opponent not connected to '"+gameID+"'")
                time.sleep(1)
                return self.playOnline(gameID)
    @classmethod
    def newOnlineGame(cls,player,gameID=""):
        if player.diceColor == BLACK:
            turn = BLACK
            board = Board(8,8)
            gameID = Board.postBoard(board)
        else :
            active,turn,board = Board.fromURL(gameID)
            Board.putBoard(True,board,turn,gameID)
        flag=0
        match = OnlineMatch(turn,player,board,Controller)
        while(not match.finished()):
            #if both self.players have no valid actions, break
            if(flag<-64):
                break;
            match.showResults()
            flag+=match.playOnline(gameID)
            os.system('clear')
            # match.nextTurn()
        match.showResults(1)
