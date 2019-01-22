EMPTY=0
BLACK=1
WHITE=2
SELECT=3

class Board:
    def __init__(self,row, col,array=[]):
        self.row=row
        self.col=col
        self.array=array
        if not array :
            for i in range(row):
                tmp=[]
                for j in range(col):
                    tmp.append(EMPTY)
                self.array.append(tmp)

            self.change(3,3,WHITE)
            self.change(4,4,WHITE)
            self.change(3,4,BLACK)
            self.change(4,3,BLACK)

    @classmethod
    def fromFile(cls,filename):
        array=[]
        with open(filename,"r") as f:
            for line in f:
                 array.append([int(c) for c in line.replace('\n','')])
        return cls(len(array),len(array[0]),array)
    @classmethod
    def fromURL(cls,gameID):
        import requests
        r = requests.get(url = "https://api.myjson.com/bins/"+gameID)
        txt = r.json()['array']
        txt = txt.split('\n')
        array=[]
        for line in txt:
             array.append([int(c) for c in line.replace('\n','')])
        return r.json()['active'],r.json()['turn'],cls(len(array),len(array[0]),array)

    @classmethod
    def putBoard(cls,active,board,turn,gameID):
        txt = ""
        for i in range(board.row):
            for j in range(board.col):
                txt+=str(board.array[i][j])
            txt+=("\n")
        txt=txt[:len(txt)-1]
        data = {"array" : txt, "turn":turn, "active" : active}
        import requests
        r = requests.put(url = "https://api.myjson.com/bins/"+gameID, json=data)
        print("https://api.myjson.com/bins/"+gameID)
        return r.content

    @classmethod
    def postBoard(cls,board):
        txt = ""
        for i in range(board.row):
            for j in range(board.col):
                txt+=str(board.array[i][j])
            txt+=("\n")
        txt=txt[:len(txt)-1]
        data = {"array" : txt, "turn" : 1, "active" : False}
        import requests
        r = requests.post(url = "https://api.myjson.com/bins/", json=data)
        return  r.json()['uri'].split('/')[-1]

    def copy(self):
        new = Board(8,8)
        new.row=self.row
        new.col=self.col
        new.array=[]
        for i in range(self.row):
            tmp=[]
            for j in range(self.col):
                tmp.append(self.array[i][j])
            new.array.append(tmp)
        return new
    def change(self, row, col, val):
        # if(val==BLACK):
        #     self.blackNum+=1
        # elif(val==WHITE):
        #     self.whiteNum+=1
        self.array[row][col]=val
    def getCount(self,val):
        c = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.array[i][j] == val:
                    c+=1
        return c

    def clearSelections(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.array[i][j] == SELECT:
                    self.array[i][j] = EMPTY
    def __str__(self):
        txt="     "
        for i in range(self.col):
            txt+=("{" + str(i) + "}  ")
        txt+="\n   "
        for j in range(self.col):
            txt+= chr(9619)+chr(9619)+chr(9619)+chr(9619)+chr(9619)
        txt+=chr(9619)+chr(9619)
        txt+=("\n")
        print("w :"+str(self.getCount(2)) + "  b :"+str(self.getCount(1)))
        for i in range(self.row):
            tmp = "{" + str(i) +"}"+chr(9619)+chr(9619)
            for j in range(self.col):
                if(self.array[i][j] == EMPTY):
                    tmp+='\033[40m' + chr(9617) + chr(9617)+chr(9617) + '\033[0m' + chr(9619) + chr(9619)
                elif (self.array[i][j] == BLACK):
                    tmp+= '\033[30m' + "   " + '\033[0m'+ chr(9619) + chr(9619)
                elif (self.array[i][j] == WHITE):
                    tmp+= '\033[37m' + chr(9608) + chr(9608)+chr(9608) + '\033[0m'+ chr(9619) + chr(9619)
                elif (self.array[i][j] == SELECT):
                    tmp+= '\033[35m' + chr(9608) + chr(9608)+chr(9608) + '\033[0m'+ chr(9619) + chr(9619)
            txt+=(tmp+"\n   ")
            for j in range(self.col):
                txt+= chr(9619)+chr(9619)+chr(9619)+chr(9619)+chr(9619)
            txt+=chr(9619)+chr(9619)
            txt+="\n"

        return txt
