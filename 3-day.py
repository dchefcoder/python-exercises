# Treasure Island Game

print('''
 *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."|` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Lola]
*******************************************************************************     
''')
      
print("Welcome to Treasure Island")
print("Your mission is to find the Treasure")
cross_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if cross_road == 'left':
    cross_left = input("You come to a lake. There is an island in the middle of the lake\nDo you want to swim or wait for a boat? Type 'swim' or 'wait'\n").lower()
    if cross_left == 'swim':
        print("There is a danger you lost the mission. Game Over!")
    elif cross_left == 'wait':
        cross_wait = input("Welcome you arrived at the island unharmed.\nThere is a house with 3 doors. One is red, yellow, and blue\nChoose the entry door color\n")
        if (cross_wait == 'red') or (cross_wait == 'blue'):
            print("Sorry you lost the mission halfway. Game Over!")
        elif cross_wait == 'yellow':
            print("Viola, You enter the room of treasure\nCongratulation you won the Game!!")      
else:  
    print("You've lost the mission. Game over!") 