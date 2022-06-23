from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(self.position()[0], (self.screen.window_height()/2) - 40)
        self.write(f"Score: {self.score}", False, "center", font=('Arial', 24, 'normal'))
    
    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write(f"Game Over", False, "center", font=('Arial', 24, 'normal'))
        
    def incriment_score(self):
        self.score += 1
        
        self.update()
        
    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Roboto', 24, 'normal'))