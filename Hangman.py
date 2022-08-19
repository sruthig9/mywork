import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''

  +---+
  |   |
 [O   |
 /|\  |
 / \  |
      |
=========''', '''

  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
      |
=========''']
#shows current hangman picture, number of incorrect guesses, and current blanks
def displayBoard(HANGMANPICS, missedLetters, correctLetters, myWord):
    print(HANGMANPICS[len(missedLetters)])
    print("you've taken "+str(len(missedLetters))+" incorrect guesses.")
    
    for letter in missedLetters:
        print(letter)

    blanks = '_' * len(myWord)

    for i in range(len(myWord)): 
        if myWord[i] in correctLetters: 
            blanks = blanks[:i] + myWord[i] + blanks[i+1:]
    print(blanks)

#gets user's guess
def getGuess(alreadyGuessedLetters):
    while True:
        guess = input("Guess a letter\n")
        guess = guess.lower()
        if len(guess) != 1:
            print("please enter a single letter!")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("please enter a letter in the alphabet")
        elif guess in alreadyGuessedLetters:
            print("you already guessed this letter.")
        else:
            return guess

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList.split())-1)
    return wordList.split()[wordIndex]

#setup words list
words = "mochi dinosaur clam cat balcony tree signature peak lightning backpack"
print("hello, let's play hangman!")
#gets random word
myWord = getRandomWord(words)
#game states
gameOver = False
correctLetters = ""
missedLetters = ""

#main loop
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, myWord)
    guess = getGuess(correctLetters+missedLetters)

    #user guesses correct letter
    if guess in myWord:
        correctLetters = correctLetters + guess

        #check whether user has guessed all the letters
        win = True
        for i in range(len(myWord)):
            if myWord[i] not in correctLetters:
                win = False
                break
        if win:
            print("Yayyyyy you've guessed the word "+myWord)
            gameOver = True
    
    #user guesses incorrect letter
    else:
        missedLetters = missedLetters + guess

        if (len(HANGMANPICS) - 1) == len(missedLetters):
            displayBoard(HANGMANPICS, missedLetters, correctLetters, myWord)
            print("You've lost!!!")
            print("The word is "+myWord)
            gameOver = True

    if gameOver:
        answer = input("Do you want to play again?\n")
        answer.lower()
        if answer == "yes":
            myWord = getRandomWord(words)
            gameOver = False
            correctLetters = ""
            missedLetters = ""
        else:
            break
