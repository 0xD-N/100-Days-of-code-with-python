import time
from turtle import Screen
from snake import Snake
from food import Food

# Screen implementation
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# snake implementation
s = Snake()
f = Food()

screen.onkeypress(s.forward, "w")
screen.onkeypress(s.angleLeft, "a")
screen.onkeypress(s.backward, "s")
screen.onkeypress(s.angleRight, "d")


# game main loop
game_is_on = True

while game_is_on:

    screen.update()
    
    s.move()

    if s.head.distance(f.position()) < 15:
        f.refresh()
    
    time.sleep(0.1)

