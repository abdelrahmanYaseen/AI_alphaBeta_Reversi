from Board import Board
EMPTY=0
BLACK=1
WHITE=2
SELECT=3

class State:
    def __init__(self,controller=None,board=None,turn=None,action=None,parent=None,val=0):
        self.board=board
        self.turn=turn
        self.controller=controller
        self.action=action
        self.parent=parent
        self.value=val
    def isTerminal(self):
        return not bool(self.controller.getActions(self.board.array,self.turn))
    def flipTurn(self):
        self.turn = BLACK if self.turn == WHITE else WHITE
    def getChildren(self):
        children=[]
        actions = self.controller.getActions(self.board.array,self.turn)
        for action in actions.keys():
            children.append(self.controller.performAction(self,action))
        return children
