import os    
import time    
    
page = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
players = 1   
   
  
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
   
Game = Running    
Mark = 'X'    
   

def DrawBoard():    
    print(" %c | %c | %c " % (page[1],page[2],page[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (page[4],page[5],page[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (page[7],page[8],page[9]))    
    print("   |   |   ")    
   
   
def CheckPoints(x):    
    if(page[x] == ' '):    
        return True    
    else:    
        return False    
   
    
def CheckWin():    
    global Game    
        
    if(page[1] == page[2] and page[2] == page[3] and page[1] != ' '):    
        Game = Win    
    elif(page[4] == page[5] and page[5] == page[6] and page[4] != ' '):    
        Game = Win    
    elif(page[7] == page[8] and page[8] == page[9] and page[7] != ' '):    
        Game = Win    
        
    elif(page[1] == page[4] and page[4] == page[7] and page[1] != ' '):    
        Game = Win    
    elif(page[2] == page[5] and page[5] == page[8] and page[2] != ' '):    
        Game = Win    
    elif(page[3] == page[6] and page[6] == page[9] and page[3] != ' '):    
        Game=Win    
        
    elif(page[1] == page[5] and page[5] == page[9] and page[5] != ' '):    
        Game = Win    
    elif(page[3] == page[5] and page[5] == page[7] and page[5] != ' '):    
        Game=Win    
        
    elif(page[1]!=' ' and page[2]!=' ' and page[3]!=' ' and page[4]!=' ' and page[5]!=' ' and page[6]!=' ' and page[7]!=' ' and page[8]!=' ' and page[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running    
    
print("Tic-Tac-Toe Game Designed By Prashant Kumar Singh")    
print("Player 1 [X] --- Player 2 [O]\n")    
print()    
print()    
print("Please Wait...")    
time.sleep(3)    
while(Game == Running):    
    os.system('cls')    
    DrawBoard()    
    if(players % 2 != 0):    
        print("Player 1's chance")    
        Mark = 'X'    
    else:    
        print("Player 2's chance")    
        Mark = 'O'    
    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
    if(CheckPoints(choice)):    
        page[choice] = Mark    
        players+=1    
        CheckWin()    
    
os.system('cls')    
DrawBoard()    
if(Game==Draw):    
    print("Game Draw")    
elif(Game==Win):    
    players-=1    
    if(players%2!=0):    
        print("Player 1 Won")    
    else:    
        print("Player 2 Won")    