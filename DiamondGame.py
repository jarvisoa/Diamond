import Diamond as d

# Game loop
while True:

	letter = input('Enter a letter to form a diamond, or "quit" to exit: ')

	if letter == "quit":
		break

	d.printDiamond(letter)

print('Have a great day!')