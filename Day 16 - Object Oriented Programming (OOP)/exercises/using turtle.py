import turtle

t = turtle.Turtle()

t.shape("turtle")

t.color("aquamarine4")


s = turtle.Screen()

print(f"\nThe screen width is: {s.window_width()}")
print(f"\nThe screen height is: {s.window_height()}")

turtle.speed(1)

turtle.forward(100)

turtle.left(90)

turtle.forward(300)

turtle.home()

s.exitonclick()