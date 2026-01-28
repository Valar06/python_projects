print(r'''                                                                          
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  ,adPPYba,
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  a8P_____88
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          8PP"""""""
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88         "8b,   ,aa
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88           `"Ybbd8"'
''') #https://ascii.co.uk/art/treasure link to this art

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("")
choice1=input('You\'re at a crossroad,where do you want to go? \n'
              'Type "Left" or "Right" \n').lower()
if choice1=="left":
    choice2=input('You\'ve come to a lake. \n'
                  'There is an island in the middle of the lake. \n'
                  'Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2=="wait":
        choice3=input('You arrive at the island unharmed. \n'
                      'There is a house with 3 doors \n'
                      '1 red 1 blue 1 yellow \n'
                      'which door will you choose: \n').lower()
        if choice3=="red":
            print("Its room full of fire. Game Over ")
        elif choice3=="yellow":
            print("You entered a room full of tigers. Game Over")
        elif choice3=="blue":
            print("You found the treasure.\n"
                  "YOU WIN!!!")
        else:
            print("You choose the door that doesn't exist. Game Over.")
    else:
        print("You got attacked by a shark ;-;")

else:
    print("You fell into a hole. Game Over.")