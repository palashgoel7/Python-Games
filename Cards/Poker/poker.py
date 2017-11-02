from deck import Deck

class Poker:
	def __init__(self, playerCount = 4):
		'''Initial card distribution'''
		self.playerCount = playerCount
		self.deck = Deck()
		self.deck.shuffle()
		self.pot = 0
		self.turn = 0

		self.playerCards = {}
		self.playersInGame = [x for x in range(playerCount)]

		for i in range(playerCount):
			self.playerCards[i] = [self.deck.pop()]

		for i in range(playerCount):
			self.playerCards[i].append([self.deck.pop()])


	def startGame(self):
		self.roundBid()

		self.deck.pop() #burn
		self.openCard = [self.deck.pop()] * 3

		self.roundBid()

		self.deck.pop() # burn
		self.openCard.append(self.deck.pop())

		self.roundBid()

		self.deck.pop() # burn
		self.openCard.append(self.deck.pop())

		self.roundBid()

	def roundBid(self):
		pass



