import random
import psycopg2


def main():
    # Our word list for the game



    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=postgres user=postgres password=evox1337")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    cur.execute("select * from public.words order by random() limit 1;")

    selectedWord = cur.fetchone()[1]
    print(selectedWord)


    conn.close()





    # selectedWord = words[random.randint(0, len(words) - 1)]
    # selecting a word at random
    
    attempts = 4
    truthTracker = False
    winningTracker = False

    scoreCorrect = 10
    scoreIncorrect = -15
    scoreCurrent = 0

    # Alternate version of doing the mask logic
    # mask = [False for char in selectedWord]

    # We are making a mask to let us know which letters should
    # or shouldn't be printing out. By default all items in the
    # List will be false. That means that those letters were not
    # guessed correctly
    mask = []
    for char in selectedWord:
        mask.append(False)

    # Our main game loop. Will not end until attempts are 0 or they won the game
    while attempts != 0 and not winningTracker:
        # Printing attempts left
        print("You have {} attempts left".format(attempts))
        print(scoreCurrent)

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
                scoreCurrent += scoreCorrect

        # Our logic for seeing if the game has been won or not
        for item in mask:
            if not item:
                winningTracker = False
                break
            else:
                winningTracker = True

        # If they guessed incorrectly, deduct an attempt
        if not truthTracker:
            attempts -= 1
            scoreCurrent += scoreIncorrect

        # Reset the truth tracker to false
        truthTracker = False

    # Printing if we won or not
    if winningTracker:
        print("You won!")
    else:
        print("You lost!")

    name = ""
    while not name.isalpha():
        print("Enter name to be saved for highscore list")
        name = input("Enter > ")

        if not name.isalpha():
            print("You gave bad bad input")

    file = open("saved", "a")
    file.write("{}, {}\n".format(name, scoreCurrent))
    file.close()


if __name__ == "__main__":
    main()
