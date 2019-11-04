import random

HANGMAN_PICS = ['''
  +---+
      |
	  |
	  |
	 ===''', '''
  +---+
  0   |
	  |
	  |
	 ===''', '''
  +---+
  0   |
  |   |
	  |
	 ===''', '''
  +---+
  0   |
  |\  |
	  |
	 ===''', '''
  +---+
  0   |
 /|\  |
	  |
	 ===''', '''
  +---+
  0  |
 /|\ |
   \ |
	 ===''', '''
  +---+
  0   |
 /|\  |
 / \  |
	 ===''']
	
# game words
words = 'ant baboon badger bat'.split()

def getRandomWord(wordList):
	wordIndex = random.randint(0, len(wordList) - 1)
	return wordList[wordIndex]
	
def displayBoard(missedLetters, correctLetters, secretWord):
	print(HANGMAN_PICS[len(missedLetters)])
	print()
	
	print('Missed letters:', end=' ')
	for letter in missedLetters:
		print(letter, end=' ')
	print()
	
	blanks = '_' * len(secretWord)
	
	for i in range(len(secretWord)):
		if secretWord[i] in correctLetters:
			blanks = blanks[:1] + secretWord[i] + blanks[i+1:]
			
	for letter in blanks:
		print(letter, end=' ')
	print()