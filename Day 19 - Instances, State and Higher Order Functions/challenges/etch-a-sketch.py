from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("aquamarine4")

screen = Screen()
screen.listen()

def forward():
    t.forward(10)
    
def backward():
    t.back(10)

def angleLeft():
    t.setheading(t.heading() + 10)
    
def angleRight():
    t.setheading(t.heading() - 10)
    

screen.onkeypress(forward, "w")
screen.onkeypress(angleLeft, "a")
screen.onkeypress(backward, "s")
screen.onkeypress(angleRight, "d")


screen.mainloop()