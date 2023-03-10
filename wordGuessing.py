# importing extra default python functionality/tools for us to use
import random

# Our word list for the game
#opening wordlist supplied by the customer
file = open("wordlist", "r")
allTheLinesOfTheFile = file.readlines()
file.close()

# Randomly selecting a word from the word list to be
# used on this run of the game. Remember we got to do
# - 1 because len() will give us the length of 4, but
# the list uses index which starts at 0 and goes to 3 (4 total)

#selectedWord = words[random.randint(0, len(words) - 1)]
#selecting a word at random
selectedWord = allTheLinesOfTheFile[random.randint(0, len(allTheLinesOfTheFile)-1)].strip()
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
    # Printing attempts left
    print("You have {} attempts left".format(attempts))

    # Printing out an _ or a char based on the mask value
    for index, char in enumerate(selectedWord):
        # If true, then print the character
        if mask[index]:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print()

    # guessing out character
    userInput = input("Guess a character > ")

    # Checking if they have us bad input
    if len(userInput) > 1 or not userInput.isalpha():
        print("You gave bad input, bad, bad person")
        continue

    # Checking if they guess a char correctly
    for index, char in enumerate(selectedWord):
        if userInput == char:
            mask[index] = True
            truthTracker = True

    # Our logic for seeing if the game has been won or not
    for item in mask:
        if not item:
            winningTracker = False
            break
        else:
            winningTracker = True

    # If they guessed incorrectly, deduct an attempt
    if not truthTracker:
        attempts = attempts - 1

# Printing if we won or not
if winningTracker:
    print("You won!")
else:
    print("You lost!")


        


    

    



        


    



    



