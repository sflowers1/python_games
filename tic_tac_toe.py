import random

def drawBoard(board):
	# 'board' is a list of 10 strings to represent the board
	# ignore index 0
	
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[1] + '|' + board[2] + '|' + board[3])
	
def inputPlayerLetter():
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print('Do you want to be X or O?')
		letter = input().upper()
		
	# first element is the players, the second is the players
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']
		
def whoGoesFirst():
	if random.randint(0,1) == 0:
		return 'computer'
	else:
		return 'player'
		
def makeMove(board, letter, move):
	board[move] = letter
	
def isWinner(bo, le):
	# bo = board, le = letter
	return (
	(bo[7] == le and bo[8] == le and bo[9] == le) or 
	(bo[4] == le and bo[5] == le and bo[6] == le) or 
	(bo[1] == le and bo[2] == le and bo[3] == le) or 
	(bo[7] == le and bo[4] == le and bo[1] == le) or 
	(bo[8] == le and bo[5] == le and bo[2] == le) or 
	(bo[9] == le and bo[6] == le and bo[3] == le) or 
	(bo[7] == le and bo[5] == le and bo[3] == le) or 
	(bo[9] == le and bo[5] == le and bo[1] == le) )
	
def getBoardCopy(board):
	boardCopy = []
	for i in board:
		boardCopy.append(i)
	return boardCopy
	
def isSpaceFree(board, move):
	return board[move] == ' '
	
def getPlayerMove(board):
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print('What is your next move? (1-9)')
		move = input()
	return int(move)
	
def chooseRandomWordFromList(board, movesList):
	possibleMoves = []
	for i in movesList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)
			
	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None
		