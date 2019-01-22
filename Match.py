from State import State
from Controller import Controller
from Board import Board
import os
import time
EMPTY=0
BLACK=1
WHITE=2
SELECT=3

class Match:
    def __init__(self,player1,player2,board,controller):
        self.player1=player1
        self.player2=player2
        self.board=board
        self.controller=controller
        self.result=0
        self.scores=(0,0)
        self.turn=player1 if player1.diceColor==BLACK else player2
        self.state=State(self.controller,board,self.turn.diceColor,None)

    def nextTurn(self):
        self.turn = self.player1 if self.turn == self.player2 else self.player2
        self.state=State(self.controller,self.board,self.turn.diceColor)
        return self.turn

    def play(self):
        import time
        # time.sleep(1)
        if self.controller.getActions(self.board.array,self.turn.diceColor):
            action = self.turn.getAction(self)
            if(self.controller.validAction(self.board.array,self.turn.diceColor,action)):
                self.state = self.controller.performAction(self.state,action)
                self.board = self.state.board
                return 0
            else :
                print("Invalid Move, try again")
                return self.play()
        else :
            # print("No valid moves : PASS")
            return -1

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
            actions = self.controller.getActions(self.board.array,self.turn.diceColor)
        else :
            actions = self.controller.getActions(self.board.array,turn)
        for act in actions:
            self.board.change(act[0],act[1],SELECT)
        print(self.board)
        self.board.clearSelections()


    @classmethod
    def newLocalGame(cls,player1,player2,activatePrints=1):
        board = Board(8,8)
        flag=0
        match = Match(player1,player2,board,Controller)
        while(not match.finished()):

            #if both players have no valid actions, break
            if(flag<-64):
                break;
            if activatePrints :
                if match.turn.diceColor == BLACK:
                    print("Black's Turn >> " + match.turn.type)

                else :
                    print("White's Turn >> " + match.turn.type)

            if activatePrints :
                match.showResults()
                match.printBoard()
            flag+=match.play()
            # os.system('clear')
            match.nextTurn()

        if activatePrints:
            os.system('clear')
            if flag < -64 :
                print("No valid move for either player")
            match.showResults(1)
            match.printBoard()
        return match.board.getCount(BLACK),match.board.getCount(WHITE)
