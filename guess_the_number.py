#guess the number game
import random

MIN = 1
MAX = 20
guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(MIN, MAX)
print('Well, ' + myName + ', I am thinking of a number between ' + str(MIN) + ' and ' + str(MAX))

for guessesTaken in range(6):
	print('Take a guess.')
	guess = input()
	guess = int(guess)
	
	if(guess < number):
		print('Too low!')
		
	elif(guess > number):
		print('Too high')
		
	else:
		break

if guess == number:
	guessesTaken = str(guessesTaken + 1)
	print('Yes! - ' + myName + '! You guessed the number in ' + guessesTaken + '.')
	
else:
	number = str(number)
	print('No! - the number I was thinking of was ' + number + '.')