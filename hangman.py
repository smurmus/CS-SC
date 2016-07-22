print("Welcome to Hangman!")
secretWord = input("Enter the secret word: ")
wordLength = int(len(secretWord))
print("Length of secret word: %i" % wordLength + "\n")
guesses = 0
counterTwo = wordLength


def isCharInString(word, letter):
    count = len(word) - 1
    while (count > 0):
        if letter in word:
            return True
        else:
            count = count - 1
    return False


def hangman_graphic(guesses):
    if guesses == 0:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")

    elif guesses == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif guesses == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif guesses == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif guesses == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
    elif guesses == 5:
       print("________      ")
       print("|      |      ")
       print("|      0      ")
       print("|     /|\     ")
       print("|     /       ")
       print("|             ")
    else:
       print("________      ")
       print("|      |      ")
       print("|      0      ")
       print("|     /|\     ")
       print("|     / \     ")
       print("|             ")

while (guesses < 6 and counterTwo != 0):
    character = str(input("Enter a letter: "))

    if (isCharInString(str(secretWord), character)):
        print(character + " IS in the secret word." + "\n")
        counterTwo = counterTwo - 1
        hangman_graphic(guesses)
        print("\n")
    else:
        print("%s is NOT in the secret word." % character)
        print("That is incorrect guess #" + str(guesses + 1) + ".\n")
        guesses = guesses + 1
        hangman_graphic(guesses)
        print("\n")

if (counterTwo == 0):
    print("You got it!")
else:
    print("Game Over.")
