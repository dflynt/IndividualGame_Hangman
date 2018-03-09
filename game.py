import random
words = ["phone", "cruise ship", "soccer", "movie", "vacation home", "road trip", "tortoise"]

wordIndex = random.randint(0,6)
word = words[wordIndex]
wordSolved = False
correctGuessedLetters = []
for i in range(0, len(word)):
    correctGuessedLetters.append(" ")
while not wordSolved:
    indexesContainingGuessedLetter = []
    choice = input("Enter a letter: ")
    if choice in word:
        #add index of letter in word to the list if guessed letter is in the word
        indexesContainingGuessedLetter = [i for i, x in enumerate(word) if x == choice]
        for x in range(0, len(indexesContainingGuessedLetter)):
            #add correctly guessed letters to their corresponding index in the mystery word
            correctGuessedLetters[indexesContainingGuessedLetter[x]] = choice
    print(" ".join(correctGuessedLetters))