class Tictactoe:
    a = [0,1,2,3,4,5,6,7,8]
    over = False
    def printBoard(self):
        print("---------------------------------------------------")
        print("  ",self.a[0],"   ||   ",self.a[1],"     ||  ",self.a[2],"    ")
        print("___________________________")
        print("  ",self.a[3],"   ||   ",self.a[4],"     ||  ",self.a[5],"    ")
        print("___________________________")
        print("  ",self.a[6],"   ||   ",self.a[7],"     ||  ",self.a[8],"    ")
        print("___________________________")
        print("       ||          ||      ")

    def userinput(self):
        print(" what do you wanna play with ? (X or O)")
        xro = input()
        if xro == 'x':
            print("where do you want to place your mark  ?")
            where = int(input("enter the position  :"))        
            self.a[where] = 'X'
        elif xro == 'o':
            print("where do you want to place your mark  ?")
            where = int(input("enter the position  :"))         
            self.a[where] = 'O'
        else:
            print(" invalied input !")
    
    def gameover(self):
        if self.a[0] == self.a[1] and self.a[1] == self.a[2]:
            print("gameover", self.a[0],"wins")
            self.over = True            
        elif self.a[3] == self.a[4] and self.a[4] == self.a[5]:
            print("gameover", self.a[3],"wins")
            self.over = True 
        elif self.a[6] == self.a[7] and self.a[7] == self.a[8]:
            print("gameover", self.a[6],"wins")
            self.over = True 
        elif self.a[0] == self.a[3] and self.a[3] == self.a[6]:
            print("gameover", self.a[0],"wins") 
            self.over = True
        elif self.a[1] == self.a[4] and self.a[4] == self.a[7]:
            print("gameover", self.a[1],"wins")
            self.over = True 
        elif self.a[2] == self.a[5] and self.a[5] == self.a[8]:
            print("gameover", self.a[2],"wins")
            self.over = True
        elif self.a[0] == self.a[4] and self.a[4] == self.a[8]:
            print("gameover", self.a[0],"wins")
            self.over = True
        elif self.a[2] == self.a[4] and self.a[4] == self.a[6]:
            print("gameover", self.a[2],"wins")
            self.over = True

tictactoe = Tictactoe()
while not tictactoe.over:          
    tictactoe.printBoard()
    tictactoe.userinput()
    tictactoe.gameover()
    