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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')

print("🏴‍☠️ Welcome to Treasure Island.")
print("Your mission is to find the treasure. 💰")

# First decision
choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right": ').lower()

if choice1 == "left":
    # Second decision
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. \n' +
                    'Type "wait" to wait for a boat or "swim" to swim across: ').lower()

    if choice2 == "wait":
        # Third decision
        choice3 = input('You arrive safely on the island. There is a house with 3 doors: one red, one yellow, and one blue.\n' +
                        'Which colour do you choose? ').lower()

        if choice3 == "red":
            print("🔥 It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("🎉 You found the treasure. You Win!")
        elif choice3 == "blue":
            print("🐺 You enter a room of wolves. Game Over.")
        else:
            print("🚪 You chose a door that doesn't exist. Game Over.")
    else:
        print("🦈 You were eaten by a shark. Game Over.")
else:
    print("💀 You fell into a hole. Game Over.")
