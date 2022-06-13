from ctypes.wintypes import RGB
import random
from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("aquamarine4")
s = Screen()
s.colormode(255)

t.pensize(15)
t.speed(10)

angles = [90, 180, 270, 0]

def randomPath(angle, length):
    
    t.pencolor(int(1 + random.random() * 255), int(1 + random.random() * 255), int(1 + random.random() * 255))
    t.setheading(angle)
    t.forward(length)
    

for _ in range(200):
    
    randomPath(random.choice(angles), 25)


s.exitonclick()