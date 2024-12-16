#This is SEASER PAPER ROCK GAME
print("!!!!!!!!!!!!WELCOME TO SCISSORS PAPAER ROCK GAME!!!!!!!!!!")
print("_______Basic Role of Game_______")
print("1. We will take no. 0,1,2 for different mode\n 0 -> ROCK\n 1 -> Paper\n 2 -> SCISSORS")

name=input("Enter the palyer Name:")

print("\n\n")
print("********START THE GAME*******")
print("___________ADD INTO GIT ___________")

import random
com = random.randint(0,2) # For computer to choose the option
# print("computer=",com)
player= int(input("Enter your choose:"))




#logic part 
if  player >=0   and player <= 2:
    if player == 0 and com == 1:
        print("Computer ---> WIN")
        print(f"{name} ---> LOSS")
    elif player == 0 and com == 2:
        print(f"{name} ---> WIN")
        print("Computer ---> LOSS")
    elif player == 0 and com == 0:
        print("Drow")
    elif player == 1 and com == 0:
        print(f"{name} ---> WIN")
        print("Computer ---> LOSS")
    elif player == 1 and com == 2:
        print("Computer ---> WIN")
        print(f"{name}---> LOSS")
    elif player == 1 and com == 1:
        print("Drow")
    elif player == 2 and com == 0:
        print("Computer ---> WIN")
        print(f"{name}---> LOSS")
    elif player == 2 and com == 1:
        print(f"{name} ---> WIN")
        print("Computer ---> LOSS")
    else:
        print("Drow")
    
else: 
    print("Invalid choose")  
