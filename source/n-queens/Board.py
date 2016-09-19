import sys

class Board:
	"""Class that especifies a chess board for n-queens problem"""


	def __init__(self, size):
		"""Constructor"""

		self.size = size								# Board of (size x size) cells with (size) queens, with size > 4
		self.state = self.initializeBoard(self.size)	# Current state of the board

	
	def initializeBoard(self, size):
		"""Function that initializes the board with a array in which each index represents
		a column and the value associated represents the row"""

		initialState = []

		# Initialize board with all queens on the 0 and 1 rows
		# alternating between even and odd column
		for i in range(0, size):
			if i%2 == 0:
				initialState.append(0)
			elif i%2 == 1:
				initialState.append(1)

		return initialState
