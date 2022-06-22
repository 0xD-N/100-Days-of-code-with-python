from turtle import Turtle

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
        t.speed(1)
        t.color("white")
        
        
        self.turtles = [t.clone() for _ in range(3)]
        
        t.hideturtle()
        
        for i in range(1, len(self.turtles)):
            
            x, y = self.turtles[i-1].position()
            self.turtles[i].setposition(x - 20, y)
            
    
    def move(self):
        """moves the snake object forward by 20 paces"""
        for i in range(len(self.turtles) -1, 0, -1):
            self.turtles[i].goto(self.turtles[i-1].position())
        
        self.head.forward(20)
        

    def angleLeft(self):
        """Turns the heading of the snake 90 degrees"""
        self.head.setheading(self.head.heading() + 90)
        
    def angleRight(self):
        """Turns the heading of the snake negative 90 degrees"""
        self.head.setheading(self.head.heading() - 90)