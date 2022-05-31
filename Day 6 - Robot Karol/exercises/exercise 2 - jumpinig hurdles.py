#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_right():
    
    turn_left()
    turn_left()
    turn_left()

#assumes bot is looking at hurdle 
def jump():
    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6):
    move()
    jump()