import json
import pathlib
from turtle import Turtle

# retrieves high score from "score" json file
def get_high_score():
    
    try:
        with open(f"{pathlib.Path(__file__).parent.resolve()}\score.json", "r") as f:
            return json.load(f)
    except IOError:
        return 0
    
 # Turtle that displays current and high score    
class Scoreboard(Turtle):
    
    
    def __init__(self):
        '''scoreboard constructor'''
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(self.position()[0], (self.screen.window_height()/2) - 40)
        self.update()
    
    # def game_over(self):
    #     self.color("red")
    #     self.goto(0,0)
    #     self.write(f"Game Over", False, "center", font=('Arial', 24, 'normal'))
        
    def reset(self):
        """Resets score and updates high score"""
        if self.score > self.high_score:
            self.high_score = self.score
        
        self.score = 0
        
        self.save_score()
        
        self.update()
    
    
    def incriment_score(self):
        """Increases score"""
        self.score += 1
        
        self.update()
    
    
    def save_score(self):
        
        """Saves score to 'score' json file in file's directory"""
        
        with open(f"{pathlib.Path(__file__).parent.resolve()}\score.json", "w") as f:
            json.dump(self.high_score, f)

            
            
    def update(self):
        """Clears the screen and writes new scores"""
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=('Roboto', 24, 'normal'))