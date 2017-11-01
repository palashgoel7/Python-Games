CROSS = 'X'
CIRCLE = 'O'
BLANK = ' '
class tictactoe:
	def __init__(self):
		self.board = [[BLANK] * 3 for i in range(3)]
		self.turn = CROSS

	def move(self, x, y):
		if x>len(self.board) or y > len(self.board[0]):
			raise IllegalMoveError("Out of bounds.")
		if self.board[x][y] != BLANK:
			raise IllegalMoveError("Square already filled.")
		self.board[x][y] = self.turn

	def switchTurn(self):
		if self.turn == CROSS:
			self.turn = CIRCLE
		else:
			self.turn = CROSS

	def checkIfWon(self):
		# Check the rows
		for row in self.board:
			if set(row) in [set(CIRCLE), set(CROSS)]:
				return True

		# Check the columns
		for i in range(3):
			if set([self.board[x][i] for x in range(3)]) in [set(CIRCLE), set(CROSS)]:
				return True

		# Check the diagonals
		if set([self.board[x][x] for x in range(3)]) in [set(CIRCLE), set(CROSS)]:
			return True

		if set([self.board[x][2-x] for x in range(3)]) in [set(CIRCLE), set(CROSS)]:
			return True

		return False

	def isBoardFull(self):
		for row in self.board:
			if BLANK in row:
				return False
		return True

	def __str__(self):
		formatStr = '''\
   |   |   
 {} | {} | {} 
   |   |   '''
		return ('\n'+"-"*11+'\n').join([formatStr.format(*row) for row in self.board])

class Error(Exception):
	'''Base Class for all exceptions'''
	pass

class IllegalMoveError(Error):
	def __init__(self, message):
		self.message = message


def Test():
	t = tictactoe()
	t.move(0,0)
	t.move(1,0)
	t.move(1,1)
	t.move(1,2)
	t.move(2,2)
	print(t)
	print(t.checkIfWon())