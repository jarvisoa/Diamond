# Global Variables
minLetter = "A"
maxLetter = "Z"
minVal = ord(minLetter)
maxVal = ord(maxLetter)

def printDiamond(letter):

	if len(letter) > 1:
		print('Please enter a single character.')
		return

	# Check for valid letter
	letterValue = ord(letter.upper())
	if minVal > letterValue or letterValue > maxVal:
		print('Please enter a letter between "A" and "Z".')
		return

	numLetters = letterValue - minVal + 1

	# Print upper half of diamond, including middle row
	printLeadorTrailLetter(numLetters)
	for k in range(1, numLetters):
		printDoubleLetterLine(k, numLetters);

	# Print lower half of diamond
	for k in range(numLetters - 2, 0, -1):
		printDoubleLetterLine(k, numLetters);

	# Do not print the same letter twice if the diamond
	# consists of a single letter
	if (minVal != letterValue):
		printLeadorTrailLetter(numLetters)

def printLeadorTrailLetter(numLetters):
	leadingSpaces = " " * numLetters
	print(leadingSpaces + minLetter)

def printDoubleLetterLine(index, numLetters):
	letter = chr(index + minVal)
	leadingSpaces = " " * (numLetters - index)
	innerSpaces = " " * (index * 2 - 1)
	print(leadingSpaces + letter + innerSpaces + letter)
	