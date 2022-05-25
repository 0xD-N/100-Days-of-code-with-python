
print("\nWelcome to treasure hunt. \nThe objective is to find the hidden treasure chest in one room.")



path = input("\nYou awake to a room with two paths. A left path and right path. Which path do you choose? (Enter left or right): ").lower()


if path == "right":
    
    choice = input("\nYou enter a room and notice a button on the podium inside of it. The button has text that says press me. Do you follow what it says? (Enter yes or no): ").lower()
    
    if choice == "yes":
        
        print("\nYou clicked the button and suddently a wall lifts up and you see 100 hungry lions. You try to leave the room from whence you came, but discover the door is locked. The lions then run towards you and slash at your torso. You then fall to the ground in a pool of blood, and shortly after the lions then begin to devour you. You have died.")

    elif choice == "no":
        
        print("\nYou chose not to press the button and a few seconds the podium retracts into the ground and out comes a treasure chest in it's place. Congragulations.")
        
        print("\n\n")
        
        print("""*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-\"""-._ ".   |
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* """)
        
    print("\nYou found the treasure! Congratulations!")

elif path == "left":
    
    choice = input("\nYou go to the path on the left and approach two doors, a red and blue door. Which door do you go through? (Enter red or blue): ").lower()
    
    if choice == "red":
        print("\nYou enter a room to what appears to be an empty room. You away from the door only to shortly fall through the floor to land in boiling lava. You have died.")
        
    elif choice == "blue":
        
        choice = input("\nYou enter the blue room to end up on the outside of the building. The surrounding looks post apocalyptic and the sun beams an orange hue. \n\n You look into the disntance and see a small figure moving towards you. As it approaches you realize it's a Deinonychus raptor. Do you run or stand still? (Enter run or stand still): ").lower()

        if choice == "run":
            print("\nThe deinonychus raptor notices you and begins running after you. You trip over a rock and fall on the ground. The raptor then catches you and devours your body. You have died.")
        elif choice == "stand still":
            print("\nThe deinonychus raptor notices something moving to his left and changes his direction of travel. You turn around and walk back to the blue door. You are now back to the main hallway.")
    
elif path == "left":
    pass
    


