from State import State
class Heuristics:
    def __init__(self):
        return

    #maximize black dices -- GREEDY
    def H1(self,state):
        state.value=state.board.getCount(1)
        # print("H1  > ", state.value, " -- ", state.turn)
        return state

    #minimize black dices
    def H2(self,state):
        state.value=64-state.board.getCount(1)
        # print("H2  > ", state.value, " -- ", state.turn)
        return state

    #minimize opponents' number of available actions
    def H3(self,state):
        counter = Heuristics.getBlacksNumberOfAvailableActions(state)
        state.value=-counter
        return state

    #combining both H1,H3 Heuristics
    def H4(self,state):
        a=1.2
        b=0.7
        state.value = a*self.H1(state).value + b*self.H3(state).value
        # print("H4  > ", state.value, " -- ", state.turn)
        return state





    @classmethod
    def getBlacksNumberOfAvailableActions(cls,state):
        # state.flipTurn()
        counter=0
        for i in range(8):
                for j in range(8):
                    if state.board.array[i][j] == 0:
                        for dir in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                            if Heuristics.search(state.board.array, j + dir[0], i + dir[1], dir,1, False):
                                counter+=1
                                break
        # state.flipTurn()
        return counter
    @classmethod
    def search(cls,array, x, y, dir, player, enemy_seen,flip=False):
        #check that we're within the boundaries of the board
        if x < 0 or x == len(array) or y < 0 or y == len(array[0]):
            return False
        #define enemy based on player
        enemy = 1 if player == 2 else 2
        #if player disk encountered
        if array[y][x] == player:
            return enemy_seen
        #if enemy disk encountered, go further with the same direction and see if we encounter the player's dice.
        if array[y][x] == enemy:
            if flip :
                array[y][x] = player
            return cls.search(array, x + dir[0], y + dir[1], dir, player, True, flip)
        return False
