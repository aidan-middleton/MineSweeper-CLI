# Author : Aidan Middleton
# Date : Aug. 10, 2022
# Description : TUI minesweeper game

import random as rand

class Mine_Sweeper():
    def __init__(self, width, height, bombs):
        #Initial game state
        self.game_over = False
        self.win = False
        
        #Dimmensions of board
        self.width = width
        self.height = height

        #Number of bombs placed
        self.bombs = bombs
        
        #Initialization
        self.board = [0] * (self.width * self.height)
        self.revealed = ["-"] * (self.width * self.height)
        self.win_board = ["-"] * (self.width * self.height)
        
        self.__generate_board__()
        self.__generate_win__()
    
    #Places the bombs and numbers around the board
    def __generate_board__(self):
        for i in range(self.bombs):
            self.valid = False
            while not self.valid:
                self.x = rand.randrange(0,self.width)
                self.y = rand.randrange(0,self.height)
                
                #Check if a bomb has already been placed here at (x,y)
                if self.board[(self.y * self.width) + self.x] != "◯":
                    
                    #Place the bomb
                    self.board[(self.y * self.width) + self.x] = "◯"
                    
                    #Update the numbers surronding the bomb 
                    for j in range(self.y-1,self.y+2):
                        for k in range(self.x-1,self.x+2):
                            if j in range(0,self.height) and k in range(0,self.width):
                                if self.board[(j * self.width) + k] != "◯":
                                    self.board[(j * self.width) + k] += 1
                    
                    #Validate that the bomb was successfully place in a unique location so that the loop may continue
                    self.valid = True
    
    #what the board will look like given the player won
    def __generate_win__(self):
        for i in range(len(self.board)):
            if self.board[i] != "◯":
                self.win_board[i] = self.board[i]
            
    #Prints the revealed portions of the board
    def __print_game__(self, board):
        print("╔%s╗"%(("═")*(self.width*2+5)))
        print("║%sMinesweeper%s║"% ((" " * int((self.width*2+5-11)/2)),(" " * int((self.width*2+5-11)/2))))
        print("╠═══╦%s═╣"% ("══" * self.width))
        print("║ - ║ ", end = '')
        for i in range(self.width):
            print("%s "% i, end = '')
        print("║")
        print("╠═══╬%s═╣"% ("══" * self.width))
        for i in range(self.height):
            print("║ %s ║ "%i, end = '')
            for j in range(self.width):
                print("%s "%board[i * self.width + j], end = '')
            print("║")
        print("╚═══╩%s═╝"% ("══" * self.width))
    
    #public interface for printing the board
    def print(self):
        self.__print_game__(self.revealed)
    
    #Public interface for starting the game
    def play_game(self):
        while not self.game_over:
            self.print()
            self.__make_move__()
        self.print()
        print("Gameover!")
        if self.win:
            print("You won!")
        else:
            print("You lost!")
    
    #Player picks a spot to sweep
    def __make_move__(self):
        self.col = input("Enter the column you would like to play in: ")
        self.row = input("Enter the row you would like to play in: ")
        self.__reveal__(int(self.col),int(self.row))
        
        if self.revealed == self.win_board:
            self.game_over = True
            self.win = True
            
    #The area specified is sweeped
    def __reveal__(self,x,y):
        if self.board[(y * self.width) + x] == "◯":
            self.revealed = self.board
            self.game_over = True
        else:
            self.revealed[(y * self.width) + x] = self.board[(y * self.width) + x]
            if self.board[(y * self.width) + x] == 0:
                for i in range(y-1,y+2):
                    for j in range(x-1,x+2):
                        if i in range(0,self.height) and j in range(0,self.width):
                            if self.board[(i * self.width) + j] != "◯":
                                if self.revealed[(i * self.width) + j] != self.board[(i * self.width) + j]:
                                    self.__reveal__(j,i)    
            
ms = Mine_Sweeper(10,10,10)
ms.play_game()