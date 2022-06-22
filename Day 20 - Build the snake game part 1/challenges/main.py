import time
from turtle import Screen, Turtle
from snake import Snake

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

screen.onkeypress(s.angleLeft, "a")
screen.onkeypress(s.angleRight, "d")

# game main loop
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()

