import random
import time
from turtle import Turtle, Screen, Vec2D

t = Turtle()
t.shape("turtle")
t.color("aquamarine4")
screen = Screen()
screen.colormode(255)
t.speed(0)

colors = [(131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]


# 10 by 10 grid

# dots 20 in size 

# spaced by 50 pixels
t.penup()
start = (-200, -200)
t.setposition(start)
t.hideturtle()

for _ in range(10):
    
    for _ in range(10):
        
        x, y = t.position()
        t.pendown()
        t.color(colors[random.randint(0, len(colors)-1)])
        t.dot(20)
        t.penup()
          
        t.setposition(x + 50, y)
        
    t.setposition(start[0], t.position()[1] + 50)
    

# exits on click
screen.exitonclick()


