print("!!!!!!!!!WELCOME TO PIG GAME!!!!!!!!!!!!")
No_player = int(input("Enter the Number of player:"))
player=[] 
score=[]
for  i in range(No_player):
    player.append(input(f"Enter the Name of {i} player:"))
    
for i in range(No_player):
    score.append(0)
    
# to roll the dic to get random no.

import random

# print(num)
game_over=False
while not game_over:
        if score[i]<=50:
        
            for i in range(No_player):
                
                print(f"*********{player[i]} Turn*********")
                on=int(input("Enter 1 to Roll the Dic:"))
                if on == 1:
                    dic =int( random.randint(1,7))
                    score[i] +=dic
                    print(f"Score={score[i]}")
                    if score[i] >= 50:
                        print(f"{player[i]} WON THE GAME ")
                        game_over=True
                        break
                    else:
                        continue
            
        
