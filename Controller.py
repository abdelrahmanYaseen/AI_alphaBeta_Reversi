from State import State
EMPTY=0
BLACK=1
WHITE=2
SELECT=3

class Controller:
    @classmethod
    def search(cls,array, x, y, dir, player, enemy_seen,flip=False):
        #check that we're within the boundaries of the board
        if x < 0 or x == len(array) or y < 0 or y == len(array[0]):
            return False
        #define enemy based on player
        enemy = WHITE if player == BLACK else BLACK
        #if player disk encountered
        if array[y][x] == player:
            return enemy_seen
        #if enemy disk encountered, go further with the same direction and see if we encounter the player's dice.
        if array[y][x] == enemy:
            if flip :
                array[y][x] = player
            return cls.search(array, x + dir[0], y + dir[1], dir, player, True, flip)
        return False
    # @classmethod
    # def flip(cls,array, x, y, dir, player, enemy_seen):
    #     #check that we're within the boundaries of the board
    #     if x < 0 or x == 8 or y < 0 or y == 8:
    #         return
    #     #define enemy based on player
    #     enemy = WHITE if player == BLACK else BLACK
    #     #if player disk encountered
    #     if array[y][x] == player:
    #         return
    #     #if enemy disk encountered, go further with the same direction and see if we encounter the player's dice.
    #     if array[y][x] == enemy:
    #         array[y][x] = player
    #         return cls.flip(array, x + dir[0], y + dir[1], dir, player, True)
    #     return

    @classmethod
    def flip(cls,array, y, x, player):

        array[y][x]=player
        #define enemy based on player
        enemy = WHITE if player == BLACK else BLACK

        counter = 0
        flag=False
        #vertical-up case
        for i in range(y-1,-1,-1):
            if array[i][x]==enemy :
                counter+=1
            elif array[i][x]==player:
                if counter>0:
                    flag = True
                break
            else :
                break
        if flag :
            for i in range(y-1,y-counter-1,-1):
                array[i][x] = player

        counter = 0
        flag=False
        #vertical-down case
        for i in range(y+1,8):
            if array[i][x]==enemy :
                counter+=1
            elif array[i][x]==player:
                if counter>0:
                    flag = True
                break
            else :
                break
        if flag :
            for i in range(y+1,y+counter+1):
                array[i][x] = player

        counter = 0
        flag=False
        #horizantal-right case
        for i in range(x+1,8):
            if array[y][i]==enemy :
                counter+=1
            elif array[y][i]==player:
                if counter>0:
                    flag = True
                break
            else :
                break
        if flag :
            for i in range(x+1,x+counter+1):
                array[y][i] = player

        counter = 0
        flag=False
        #horizantal-left case
        for i in range(x-1,-1,-1):
            if array[y][i]==enemy :
                counter+=1
            elif array[y][i]==player:
                if counter>0:
                    flag = True
                break
            else :
                break
        if flag :
            for i in range(x-1,x-counter-1,-1):
                array[y][i] = player

        #diagonal-up-right case
        counter = 0
        flag=False
        c = 0
        tmpx=x+1
        tmpy=y-1
        while (tmpx!=8) and (tmpy!=-1) and (tmpx!=-1) and (tmpy!=8) :
            if array[tmpy][tmpx]==enemy :
                counter+=1
            elif array[tmpy][tmpx]==player:
                if counter>0:
                    flag = True
                break
            else :
                break
            tmpx+=1
            tmpy-=1
        tmpx=x+1
        tmpy=y-1
        if flag :
            for i in range(counter):
                array[tmpy][tmpx] = player
                tmpx=tmpx+1
                tmpy=tmpy-1

        #diagonal-up-left case
        counter = 0
        flag=False
        c = 0
        tmpx=x-1
        tmpy=y-1
        while (tmpx!=8) and (tmpy!=-1) and (tmpx!=-1) and (tmpy!=8) :
            if array[tmpy][tmpx]==enemy :
                counter+=1
            elif array[tmpy][tmpx]==player:
                if counter>0:
                    flag = True
                break
            else :
                break
            tmpx-=1
            tmpy-=1
        tmpx=x-1
        tmpy=y-1
        if flag :
            for i in range(counter):
                array[tmpy][tmpx] = player
                tmpx=tmpx-1
                tmpy=tmpy-1
        #diagonal-down-right case
        counter = 0
        flag=False
        c = 0
        tmpx=x+1
        tmpy=y+1
        while (tmpx!=8) and (tmpy!=-1) and (tmpx!=-1) and (tmpy!=8) :
            if array[tmpy][tmpx]==enemy :
                counter+=1
            elif array[tmpy][tmpx]==player:
                if counter>0:
                    flag = True
                break
            else :
                break
            tmpx+=1
            tmpy+=1
        tmpx=x+1
        tmpy=y+1
        if flag :
            for i in range(counter):
                array[tmpy][tmpx] = player
                tmpx=tmpx+1
                tmpy=tmpy+1

        #diagonal-down-left case
        counter = 0
        flag=False
        c = 0
        tmpx=x-1
        tmpy=y+1
        while (tmpx!=8) and (tmpy!=-1) and (tmpx!=-1) and (tmpy!=8) :
            if array[tmpy][tmpx]==enemy :
                counter+=1
            elif array[tmpy][tmpx]==player:
                if counter>0:
                    flag = True
                break
            else :
                break
            tmpx-=1
            tmpy+=1
        tmpx=x-1
        tmpy=y+1
        if flag :
            for i in range(counter):
                array[tmpy][tmpx] = player
                tmpx=tmpx-1
                tmpy=tmpy+1

        # #check that we're within the boundaries of the board
        # if x < 0 or x == 8 or y < 0 or y == 8:
        #     return
        # #if player disk encountered
        # if array[y][x] == player:
        #     return
        # #if enemy disk encountered, go further with the same direction and see if we encounter the player's dice.
        # if array[y][x] == enemy:
        #     array[y][x] = player
        #     return cls.flip(array, x + dir[0], y + dir[1], dir, player, True)
        # return
    @classmethod
    def getActions(cls,array,player):
        actions={}
        for i in range(8):
                for j in range(8):
                    if array[i][j] == EMPTY:
                        #for all the surroundings of the empty place
                        for dir in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                            if cls.search(array, j + dir[0], i + dir[1], dir, player, False):
                                actions[(i,j)]=dir
                                break
        return actions

    @classmethod
    def analyzeBoard(cls,array):
        whiteNum=0
        blackNum=0
        emptyNum=0
        for i in range(8):
                for j in range(8):
                    if array[i][j]== WHITE:
                        whiteNum+=1
                    elif array[i][j] == BLACK:
                        blackNum+=1
                    else:
                        emptyNum+=1
        return whiteNum,blackNum,emptyNum

    @classmethod
    def validAction(cls,array,player,action):
        try:
            a = cls.getActions(array,player)[action]
            if a :
                return True
        except Exception:
            return False

    @classmethod
    def performAction(cls,state,action):
        tmpBoard=state.board.copy()
        if action :
           validActions=Controller.getActions(tmpBoard.array,state.turn)
           tmpBoard.change(action[0],action[1],state.turn)
           # cls.flip2(tmpBoard.array,action[1]+validActions[action][0],action[0]+validActions[action][1],validActions[action],state.turn,False)
           cls.flip(tmpBoard.array,action[0],action[1],state.turn)
           # enemey = WHITE if player == BLACK else BLACK
        return State(cls,tmpBoard,state.turn,action,state)
