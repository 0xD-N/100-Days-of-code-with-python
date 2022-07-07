import tkinter

# creating initial top window
window = tkinter.Tk()

#changing window title
window.title("My first GUI")

#setting minimum size of window
window.minsize(width=500, height=300)

### creating a label component ###
label1 = tkinter.Label(window, text="Ayo wats good", font=("Ariel", 24,  "bold"))

# adds to screen label
label1.pack()

# configures label and changes text to new text
label1.config(text="Dis is new text now")

#########################################

### button component ###

# function to be executed when button is clicked
def on_click():
    
    label1.config(text=inputBox.get())

# command is executed when mouse button 1 (left click button) is released over the button, simulating a click. The command associated is the on_click function
btn = tkinter.Button(window, text="Click me", command=on_click)
btn.pack()
################################################################

### Entry component ###

inputBox = tkinter.Entry(window)

inputBox.pack()

################################################################

### text component ###

txtBox = tkinter.Text(window, width=30, height=5)
txtBox.pack()

#http://www.tcl-lang.org/man/tcl8.6/TkCmd/text.htm#M24
#inserting text on line 1, character position 0
txtBox.insert(1.0, "Here we go")

#http://www.tcl-lang.org/man/tcl8.6/TkCmd/text.htm#M147
print(txtBox.search("we", 0.0, tkinter.END))

################################################################

### Spinbox component ###

def spinbox_on_change():
    print(spinbox.get())

spinbox = tkinter.Spinbox(window, from_ = 1, to=10, command=spinbox_on_change)
spinbox.pack()
################################################################

### Scale component ###

def scale_on_change(value):
    
    print(value)
    
    
scale = tkinter.Scale(window, from_= 1, to=100, command = scale_on_change)
scale.pack()

################################################################

### Checkbutton component ###

is_enabled = tkinter.IntVar(window)

def checkbox_interacted():
    print("interacted")
    print(f"The state of the checkbox is: {is_enabled.get()}")
    
checkbox = tkinter.Checkbutton(window, text="Click me", command=checkbox_interacted, variable=is_enabled)
checkbox.pack()
################################################################

### Radio button component ###

radio_state = tkinter.IntVar(window)

def radio_interacted():
    print("interacted")
    print(f"The state of the radio button is: {radio_state.get()}")

radio_button1 = tkinter.Radiobutton(window, value=1, command=radio_interacted, variable=radio_state, text="one")
radio_button2 = tkinter.Radiobutton(window, value=2, command=radio_interacted, variable=radio_state, text="two")
radio_button3 = tkinter.Radiobutton(window, value=3, command=radio_interacted, variable=radio_state, text="three")
radio_button4 = tkinter.Radiobutton(window, value=4, command=radio_interacted, variable=radio_state, text="four")

radio_button1.pack()
radio_button2.pack()
radio_button3.pack()
radio_button4.pack()

window.mainloop()