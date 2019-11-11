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
	print())
	
	print('Missed letters:', end=' ')
	for letter in missedLetters:
		print(letter, end=' ')
	print()
	
	blanks = '_' * len(secretWord)
	
	for i in range(len(secretWord)):
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
			
	for letter in blanks:
		print(letter, end=' ')
	print()
	
def getGuess(alreadyGuessed):
	#make sure the player enters a single letter and nothing else
	while True:
		print('Guess a letter.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print('Please enter a single letter.')
		elif guess in alreadyGuessed:
			print('You have already guessed this letter.')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('Please enter a LETTER.')
		else:
			return guess

def playAgain():
	print('Play again?')
	return input().lower().startswith('y')
	

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
	displayBoard(missedLetters, correctLetters, secretWord)
	
	#enter a letter
	guess = getGuess(missedLetters + correctLetters)
	
	if guess in secretWord:
		correctLetters = correctLetters + guess
		
		#check if player has won
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		
		if foundAllLetters:
			print('Yes!The secret word is ' + secretWord)
			gameIsDone = True
			
	else:
		missedLetters = missedLetters + guess
		
		#check if player has lost
		if len(missedLetters) == len(HANGMAN_PICS) - 1:
			displayBoard(missedLetters, correctLetters, secretWord)
			print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + 
			' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + 
			secretWord + '"')
			gameIsDone = True
			
	# ask the player if they want to play again
	if gameIsDone:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameIsDone = False
			secretWord = getRandomWord(words)
		else:
			break
			