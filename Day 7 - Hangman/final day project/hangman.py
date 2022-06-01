from os import system
import random


stages = ['''
  +---+  
  |   |  
      |  
      |  
      |  
      |  
=========
''', '''
  +---+  
  |   |  
  O   |  
      |  
      |  
      |  
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

wordBank = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

secretWord = random.choice(wordBank)

secretWordPlaceholder = ["_" for _ in range(len(secretWord))]

stage = 0

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)

print("\n")

while "_" in secretWordPlaceholder and stage != 6:
    
    print(stages[stage])
    
    print(" ".join(secretWordPlaceholder))
    
    guess = input("\nEnter guess: ").lower()
    
    if guess in secretWord:
        
        for index in range(len(secretWord)):
            if secretWord[index] == guess:
                secretWordPlaceholder[index] = guess
    
    else:
        stage += 1
    
    system("cls")

if stage != 6 and "_" not in secretWordPlaceholder:
    
    print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)
    
    print(f"\nCongratulations! You guess the word. The word was {secretWord}.")
else:
    
    print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)
    
    print("\nYou lose!")
    
