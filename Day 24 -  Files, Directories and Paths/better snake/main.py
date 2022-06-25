import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen implementation
screen = Screen()
screen.setup(width=620, height=620)
screen.colormode(255)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# snake, food, and Scoreboard implementation
s = Snake()
f = Food()
score = Scoreboard()

screen.onkeypress(s.up, "w")
screen.onkeypress(s.left, "a")
screen.onkeypress(s.down, "s")
screen.onkeypress(s.right, "d")


# game main loop
game_is_on = True

while game_is_on:

    screen.update()
    
    s.move()
    
    xPos, yPos = s.head.position()

    # wall collision detection
    if xPos >= (screen.window_width()/2) or xPos < -(screen.window_width()/2) or yPos >= (screen.window_height()/2) or yPos < -(screen.window_height()/2) + 10:
        score.reset()
        s.reset()

    else:
        # body collision detection
        for i in range(1, len(s.turtles)): 
            if s.head.distance(s.turtles[i].position()) < 10:
                score.reset()
                s.reset()
                break
    
    # food collision detection        
    if s.head.distance(f.position()) < 15:
        score.incriment_score()
        s.extend()
        f.refresh()

    time.sleep(0.05)

screen.exitonclick()