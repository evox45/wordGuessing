# importing extra default python functionality/tools for us to use
import random

# Our word list for the game
words = ["process", "thread", "forks", "signal"]

# Randomly selecting a word from the word list to be
# used on this run of the game. Remember we got to do
# - 1 because len() will give us the length of 4, but
# the list uses index which starts at 0 and goes to 3 (4 total)

#selectedWord = words[random.randint(0, len(words) - 1)]

selectedWord = words [random.randint(0, len(words)-1)]
attempts = 5
truthTracker = False
winningTracker = False

# Alternate version of doing the mask logic
# mask = [False for char in selectedWord]

# We are making a mask to let us know which letters should
# or shouldn't be printing out. By default all items in the 
# List will be false. That means that those letters were not
# guessed correctly
mask = []
for char in selectedWord:
    mask.append(False)

# Our main game loop. Will not end untill attemps are 0 or they won the game
while attempts != 0 and not winningTracker:
    # Printing attemps left
    print("you have {} attempts left".format (attempts))
    # Printing out characters on the screen. The chars may be _ or
    # and char for the word. We need to do enumerate to get the index
    # so we can keep our work and mask synced up
    for index, char in enumerate(selectedWord):
        # If true, then print the character
        if mask[index]:
            print(char, end=" ")
        # If false or anything else, print an _
        else:
            print("_", end=" ")
    # Printing a new line because we have a custom end=
    print()

    # Getting the user's input
    userInput = input("Guess a character > ")

    # Our logic for filtering out bad input. This will be looking
    # For anything that is longer than 1 character, or is not a
    # alphabetical character
    if len(userInput) > 1 or not userInput.isalpha():
        print("You gave bad input, bad, bad person")
        continue
    #checking if they guessed a char correctly
    for index, char in enumerate(selectedWord):
        if userInput == char:
            mask[index] = True
            truthTracker = True
            print("They guess a char correctly")


    # Our logic for seeing if the game has been won or not
    for item in mask:
        if not item:
            winningTracker = False
            break
        else:
            winningTracker = True
            

        # If they guessed incorrectly, detuct an attempt
    if not truthTracker:
        attempts = attempts -1

# If we won or not
if winningTracker:
    print("You won!")

else:
    print("You lost!")



# Challange remake the game

        


    

    
   


        


    
   


    



   