SYMBOLS = 'ABCDEFGHIJKMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
	while True:
		print('Do you wish to encrypt(e) or decrypt(d)?')
		mode = input().lower()
		if mode in ['encrypt', 'e', 'decrypt', 'd']:
			return mode

def getMessage():
	print('Enter your message')
	return input()
	
def getKey():
	key = 0
	while True:
		print('Enter the key number (1 - %s)' %(MAX_KEY_SIZE))
		key = int(input())
		if(key >= 1 and key <= MAX_KEY_SIZE):
			return key

def getTranslatedMessage(mode, message, key):
	if mode[0] == 'd':
		key = -key
	translated = ''
	
	for symbol in message:
		symbolIndex = SYMBOLS.find(symbol)
		if symbolIndex == -1: 	#not found
			translated += symbol
		else:
			symbolIndex += key
	
	
		if symbolIndex >= len(SYMBOLS):
			symbolIndex -= len(SYMBOLS)
		elif symbolIndex < 0:
			symbolIndex += len(SYMBOLS)
			
		translated += SYMBOLS[symbolIndex]
	return translated
	
mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))