# IndividualGame_Hangman
This game gives the player a secret word and the player will guess letters to figure out the word.
Upon running it, the console will print a varying number of underscores _ based on the word length.
The user has an infinite number of guesses and after each successful letter guess, the letter will replace
the underscore.

Example:

After running game.py:

_ _ _ _ _

After a successful guess:

_ _ _ i _

After solving the puzzle:

m o v i e

Puzzle Solved!

Program Flow:
Use a random number generator to generate a number from 0-6 and retrieve a word from the words[] list. Depending on the length of the word, make a string of only underscores and spaces depending on the puzzle.

Prompt the user with a message saying "Enter a letter: ". If the guessed letter is in the puzzle, get the indexes of that letter and insert the letter into the list containing the underscores and begin populating it with the correct letters in their corresponding indexes
.