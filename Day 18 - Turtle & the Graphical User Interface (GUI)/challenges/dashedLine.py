from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("aquamarine4")


t.speed(1)
#draws a square
for _ in range(15):
    
    t.forward(10)
    t.up()
    t.forward(10)
    t.down()



# To exit on click
screen = Screen()
screen.exitonclick()


