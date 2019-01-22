import random
from State import State
INFINITY = float('Inf')
EMPTY=0
BLACK=1
WHITE=2
SELECT=3
class HumanAgent:
    def __init__(self,diceColor):
        self.type="HumanAgent"
        self.diceColor=diceColor
        return
    def getAction(self,match):
        txt = input("Enter (row,column) :")
        txt=txt.split(",")
        return (int(txt[0]),int(txt[1]))


class RandomAgent:
    def __init__(self,diceColor):
        self.type="RandomAgent"
        self.diceColor=diceColor
        return
    def getAction(self,match):
        import time
        time.sleep(.1)
        return random.choice(list(match.controller.getActions(match.board.array,self.diceColor)))



class MinimaxAgent:
    def __init__(self, diceColor, max_depth,H):
        self.type="minimaxAgent"
        self.diceColor=diceColor
        self.max_depth = max_depth
        self.H=H

    def minimax(self,state, depth, maxPlayer):
        if depth==0 or state.isTerminal():
            return self.H(state)
        if maxPlayer:
            val = State(None,None,None,None,None,-INFINITY)
            if state.getChildren():
                for child in state.getChildren() :
                    newVal=self.minimax(child,depth-1,False)
                    if(val.value <= newVal.value):
                        val = newVal
                return val
            else :
                return self.H(state)
        else :
            val = State(None,None,None,None,None,INFINITY)
            if state.getChildren():
                for child in state.getChildren():
                    newVal=self.minimax(child,depth-1,True)
                    if(val.value >= newVal.value):
                        val = newVal
                return val
            else :
                return self.H(state)


    def minimaxAB(self,state, depth,alpha, beta, maxPlayer):
        if depth==0 or state.isTerminal():
            return self.H(state)
        if maxPlayer :
            val = State(None,None,None,None,None,-INFINITY)
            if state.getChildren():
                for child in state.getChildren() :
                    newVal=self.minimaxAB(child,depth-1,alpha,beta,False)
                    if(val.value <= newVal.value):
                        val = newVal
                    alpha = max(alpha,val.value)
                    if(alpha >= beta):
                        break
                return val
            else :
                return self.H(state)
        else :
            if state.getChildren():
                val = State(None,None,None,None,None,INFINITY)
                for child in state.getChildren():
                    newVal=self.minimaxAB(child,depth-1,alpha,beta,True)
                    if(val.value >= newVal.value):
                        val = newVal
                    beta = min(beta,val.value)
                    if(alpha >= beta):
                        break
                return val
            else :
                return self.H(state)
            return val

    def getAction(self,match):
        # state=self.minimax(match.state, self.max_depth, match.state.turn==BLACK)
        print("IN MINIMAx")
        # print(match.state.turn)
        # print(match.state.board)
        # for i in match.state.getChildren():
        #     print(i.action)
        #     print(i.board)
        match.state.parent=None
        state=self.minimaxAB(match.state, self.max_depth,-INFINITY,INFINITY,match.state.turn==BLACK)
        
        if state.parent :
            print("AFTER COMP")
            while(state.parent.parent!=None):
                print(state.action)
                print(state.board)
                state=state.parent
            print(state.action)
            print(state.board)
        # input()
        if not state.action :
            print("error ! : ")
            exit(1)
            return random.choice(list(match.controller.getActions(match.board.array,self.diceColor)))

        # print("------------------")
        # for child in match.state.getChildren() :
        #     print(child.action)
        #     print(child.board)
        # print("-------end----------")
        # print(state.action)
        # input()
        return state.action
