import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
	#returns a unique string of random digits that is NUM_DIGITS long
	numbers = list(range(10))
	random.shuffle(numbers)
	secretNum = ''
	for i in range(NUM_DIGITS):
		secretNum += str(numbers[i])
	return secretNum
	
def getClues(guess, secretNum):
	#returns a string with the pico, fermi, or bagels clues
	if guess == secretNum:
		return 'You got it!'
		
	clues = []
	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			clues.append('Fermi')
		elif guess[i] in secretNum:
			clues.append('Pico')
	if len(clues) == 0:
		return 'bagels'
		
	clues.sort()
	return ' '.join(clues)
	
def isOnlyDigits(num):
	if num == '':
		return False
	
	for i in num:
		if i not in '0 1 2 3 4 5 6 7 8 9'.split():
			return False
			
	return True
	
#game loop
print('I am thinking of a %s-digit number... Try to guess what it is.' %(NUM_DIGITS))
print('The clues I give are...')
print('When I say:    Tha means:')
print('  bagels     None of the digits are correct')
print('  pico       One digit is correct in the wrong position')
print('  fermi      One digit is correct and in the right position')

while True:
	secretNum = getSecretNum()
	print('I have thought of a number, you have %s guesses to get it.' %(MAX_GUESS))
	
	guessesTaken = 1
	while guessesTaken <= MAX_GUESS:
		guess = ''
		while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
			print('Guess #%s: ' %(guessesTaken))
			guess = input()
			
		print(getClues(guess, secretNum))
		guessesTaken += 1
		
		if guess == secretNum:
			break
		if guessesTaken > MAX_GUESS:
			print('You ran out of guesses, the answer was %s.' %(secretNum))
			
	print('Play again?')
	if not input().lower().startswith('y'):
		break
		
	
		