import pandas as pd
import pathlib as pb
import turtle


CURRENT_FILE_LOCATION = pb.Path(__file__)

def setup() -> dict:
    
    data = pd.read_csv(CURRENT_FILE_LOCATION.parent / "50_states.csv").to_dict("list")
    
    output = {}
    
    s = [x.lower() for x in data["state"]]
    x_coords = [x for x in data["x"]]
    y_coords = [y for y in data["y"]]
    
    for i in range(len(s)):
        output.update({s[i]: (x_coords[i], y_coords[i])})
        
    return output

def setup_turtle():
    
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    
    return t;

class Game:
    
    def __init__(self):
        
        self.states: dict = setup()
    
        self.turtle: turtle.Turtle = setup_turtle()
        
        self.score: int = 0
        
        self.states_original_length = len(self.states)
        
    def start(self):
        
        while len(self.states) != 0:
            
            guess = turtle.textinput(f"Guess the State ({self.score}/{self.states_original_length})", "What is another state's name?").lower().strip()
            
            if guess in self.states:
                
                x, y = self.states[guess]
                self.turtle.goto(x - 20, y)
                
                self.turtle.pendown()
                self.turtle.write(guess.capitalize(), False, "left", font=('Arial', 8, 'normal'))
                self.turtle.penup()
                
                self.states.pop(guess)
                
                self.score += 1
            
            
            
            
            