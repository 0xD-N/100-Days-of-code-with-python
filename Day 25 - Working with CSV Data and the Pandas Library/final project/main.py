import turtle
from pathlib import Path
from game import Game


screen = turtle.Screen()

screen.setup(width=1100, height=720)
screen.title("U.S States Game")

#pathlib file object
current_file_location = Path(__file__)

# getting location of local csv
blank_states_image_location = current_file_location.parent / "blank_states_img.gif"

# adding image to turtle
screen.addshape(f"{blank_states_image_location}")

#setting 
turtle.shape(f"{blank_states_image_location}")

game = Game()

game.start()

turtle.mainloop()