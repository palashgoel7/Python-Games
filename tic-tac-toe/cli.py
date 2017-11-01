from engine import tictactoe, IllegalMoveError

print("Lets play a game of tic-tac-toe")
print("Rules:")
print(
'''\t1. Cross starts the game.
\t2. Players alternate turns.
\t3. To win, player must get his token on all cells in a straight line
\t4. Game ends when either player wins or there are no more empty cells''')

t = tictactoe()
while True:
	print("Current Turn: {}".format(t.turn))
	print(t)
	while True:
		x,y = list(map(int, input("Enter your choice: ").split()))
		try:
			t.move(x,y)
			break
		except IllegalMoveError as e:
			print("Illegal move: ", e)

	if t.checkIfWon():
		print(t)
		print(t.turn, "won. Congratulations!!")
		break

	if t.isBoardFull():
		print("The board is full. Game ends in a draw!")

	t.switchTurn()