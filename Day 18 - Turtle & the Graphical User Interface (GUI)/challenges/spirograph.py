import random
from turtle import Turtle, Screen

t = Turtle()
t.shape("arrow")
t.color("aquamarine4")
s = Screen()
s.colormode(255)


t.speed(0)


def randColor():
    
    r = int(1 + random.random() * 255)
    g = int(1 + random.random() * 255)
    b = int(1 + random.random() * 255)
    
    return (r,g,b)

# the range should be 360 divided by the difference in angles between each circle
for _ in range(60):
    
    t.pencolor(randColor())
    t.circle(100, 360)
    t.setheading(t.heading() - 6)









s.exitonclick()