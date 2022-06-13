import random
from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("aquamarine4")

shapes = {
    "triangle": 3,
    "square": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10,
}

colors = ["orange", "red", "aquamarine4", "gray", "wheat", "medium spring green", "magenta", "black", "blue"]

def drawShape(sides, length):
    
    angle = 360/sides
    
    t.color(random.choice(colors))
    
    for _ in range(sides):
        t.forward(length)
        t.right(angle)
        

drawShape(shapes["triangle"], 100)
drawShape(shapes["square"], 100)
drawShape(shapes["pentagon"], 100)
drawShape(shapes["hexagon"], 100)
drawShape(shapes["heptagon"], 100)
drawShape(shapes["octagon"], 100)
drawShape(shapes["nonagon"], 100)
drawShape(shapes["decagon"], 100)



# To exit on click
screen = Screen()
screen.exitonclick()


