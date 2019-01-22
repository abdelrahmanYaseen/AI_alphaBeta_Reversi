import random
class RandomAgent:
    def __init__(self,diceColor):
        self.diceColor=diceColor
        return
    def getAction(self,match):
        return random.choice(list(match.controller.getActions(match.board.array,self.diceColor)))
