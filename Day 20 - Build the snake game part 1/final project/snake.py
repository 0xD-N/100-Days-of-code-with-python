from turtle import Turtle
import random

def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r,g,b)

class Snake():
    
    
    def __init__(self):
        """Snake constructor"""
        self.turtles: list[Turtle] = []
        self.initialize_snake()
        self.head = self.turtles[0]
    
    def initialize_snake(self):
        
        """Initializes snake"""
        t = Turtle()
        t.penup()
        t.shape("square")
        t.speed(0)
        t.color("white")
        
        
        self.turtles = [t.clone() for _ in range(3)]
        
        t.hideturtle()
        
        for i in range(1, len(self.turtles)):
            
            x, y = self.turtles[i-1].position()
            self.turtles[i].setposition(x - 20, y)
            
        for turtle in self.turtles:
            turtle.color(get_color())
      
    def extend(self):
        """Extends snake body"""
        c = self.head.clone()
        c.color(get_color())
        self.turtles.append(c)
          
    def move(self):
        """moves the snake object forward by 20 paces"""
        for i in range(len(self.turtles) -1, 0, -1):
            self.turtles[i].goto(self.turtles[i-1].position())
        
        self.head.forward(20)
        
    def up(self):
        """Turns the heading of the snake 90 degrees"""
        if self.head.heading() != 270 and self.head.heading() != -90:
            self.head.setheading(90)
            
    def down(self):
        """Turns the heading of the snake 270 degrees"""
        if self.head.heading() != 90 and self.head.heading() != -270:
            self.head.setheading(270)
            
    def left(self):
        """Turns the heading of the snake 180 degrees"""
        if self.head.heading() != 0:
            self.head.setheading(180)
        
    def right(self):
        """Turns the heading of the snake 0 degrees"""
        if self.head.heading() != 180 and self.head.heading() != -180:
            self.head.setheading(0)