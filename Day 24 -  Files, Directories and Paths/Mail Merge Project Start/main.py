import pathlib
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# https://docs.python.org/3/library/pathlib.html
p = pathlib.Path(__file__)

# get starting_letter folder
starting_letter = (p.parent / "Input" / "Letters" / "starting_letter.txt").resolve()

# get file with list of names
names_file = (p.parent / "Input" / "Names" / "invited_names.txt").resolve()

# holds the content of the letter file
letter = []

# holds the content of the names file
names = []

# opens starting letter, saves each line into letter list
with open(starting_letter, "r") as f:
    
    letter = f.readlines()

# opens names file and saves each line in the names list
with open(names_file, "r") as f:
    names = f.readlines()
    
# retrieve ReadyToSend folder
ready_to_send_folder = (p.parent / "Output" / "ReadyToSend").resolve()

# for each name in names create a new file and write the content from the letter, replacing [name] with name from "names" list
for name in names:
    
    n = name.replace("\n", "")
    with open(ready_to_send_folder / f"letter_for_{n}.txt", "w") as f:
        
        # copy letter
        copy = letter[:]
        copy[0] = copy[0].replace("[name]", name.replace("\n", ""))
        
        for line in copy:
            f.write(line)
    