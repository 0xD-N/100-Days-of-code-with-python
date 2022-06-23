from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1.0,1.0)
        self.color("blue")
        self.penup()
        self.refresh()
    
    def refresh(self):
        
        screen = self.screen
        x = random.randint(-(screen.window_width()/2) + 25, (screen.window_width()/2) - 25)
        y = random.randint(-(screen.window_height()/2) + 25, 270)
        
        self.setposition((x,y))
        