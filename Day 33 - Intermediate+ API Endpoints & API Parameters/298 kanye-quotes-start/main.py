from tkinter import *
import requests
import pathlib

def get_quote():
    
    
    response = requests.get("https://api.kanye.rest/")
    
    response.raise_for_status()
    
    json_data = response.json()

    canvas.itemconfig(quote_text, text=json_data["quote"])
    

CURRENT_FILE_DIRECTORY = pathlib.Path(__file__)

kanye_image = CURRENT_FILE_DIRECTORY.parent / "kanye.png"

background_image = CURRENT_FILE_DIRECTORY.parent / "background.png"


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=background_image)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=kanye_image)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()