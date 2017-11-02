from itertools import product
import random
class Deck:
	def __init__(self, Suits = ['Spade', 'Heart', 'Club', 'Diamond'],
				FaceValue = ([x for x in range(2,11)])):
		FaceValue.extend(['Jack', 'Queen', 'King', 'Ace'])
		self.deck = [x for x in product(Suits, FaceValue)]

	def shuffle(self):
		random.shuffle(self.deck)

	def pop(self):
		if self.isEmpty():
			raise Exception("Deck Empty")
		return self.deck.pop()

	def isEmpty(self):
		return len(self.deck) == 0

