import random
from turtle import Screen, Turtle

t = Turtle()
t.penup()
t.shape("turtle")
t.speed(0)

#initial screen setup
screen = Screen()
screen.setup(width=1000, height=600)
screen.colormode(255)
screen.title("Turtle race")


#set turtle position
t.goto(-((screen.window_width()-18) / 2), (screen.window_height() - 25) / 2)

#generates copies of turtle
turtles: list[Turtle] = [t.clone() for _ in range(12)]

colors = ["orange", "red", "aquamarine4", "gray", "wheat", "medium spring green", "magenta", "black", "blue", "brown", "yellow", "green", "purple"]

#randomizes color for each turtle
for turtle in turtles:
    
    turtle.color(random.choice(colors))

#hide the original turtle as its not used anymore
t.hideturtle()

# puts each turtle 50 spaces below one another
for i in range(1, len(turtles)):
    
    turtles[i].goto(turtles[i-1].position()[0],turtles[i-1].position()[1] - 50) 

user_gamble = screen.textinput("Place your bet", "Which color turtle do you think will win?")
#race logic
def race(turtles: list[Turtle]):
    
    over = False
    winner = None
    
    while not over:
        
        for turtle in turtles:
            
            turtle.forward(random.randint(5,50))
            if turtle.position()[0] >= screen.window_width()/2:
                over = True
                winner = turtle
                break
        pass
    
    return winner

r = race(turtles)

for turtle in turtles:
    
    turtle.hideturtle()

r.showturtle()

r.home()

print()
if r.color()[0] != user_gamble.lower():
    print(f"sorry, {r.color()[0]} turtle won.")
else:
    print(f"You won! The {r.color()[0]} turtle won!")


screen.exitonclick()
