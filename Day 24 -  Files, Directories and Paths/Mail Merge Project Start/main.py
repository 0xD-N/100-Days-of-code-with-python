import pathlib
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

p = pathlib.Path(__file__)

starting_letter = (p.parent / "Input" / "Letters" / "starting_letter.txt").resolve()

names_file = (p.parent / "Input" / "Names" / "invited_names.txt").resolve()


letter = []
names = []

with open(starting_letter, "r") as f:
    
    letter = f.readlines()

with open(names_file, "r") as f:
    names = f.readlines()
    

ready_to_send_folder = (p.parent / "Output" / "ReadyToSend").resolve()

for name in names:
    
    n = name.replace("\n", "")
    with open(ready_to_send_folder / f"letter_for_{n}.txt", "w") as f:
        
        copy = letter[:]
        copy[0] = copy[0].replace("[name]", name.replace("\n", ""))
        
        for line in copy:
            f.write(line)
    