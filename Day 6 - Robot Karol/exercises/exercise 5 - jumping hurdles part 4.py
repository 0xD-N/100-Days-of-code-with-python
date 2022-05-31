def turn_right():
    
    turn_left()
    turn_left()
    turn_left()

def jump():
    
    turn_left()
    move()
    turn_right()
    
    if wall_in_front():
       
       while wall_in_front():
           turn_left()
           move()
           turn_right()
           
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    
    if wall_in_front():
        jump()
    else:
        if at_goal():
            break
        else:
            move()