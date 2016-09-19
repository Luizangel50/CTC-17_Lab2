import math


def calculateCost(board):
	"""Function that calculates the cost of the board's state"""

	cost = 0

	for i in range(0, board.size):
		cost += calculateNeighbors(board, i)

	return cost

def calculateNeighbors(board, currentCell):
	"""Auxiliar function that return the number of neighbors
	of currentCell on the board"""

	neighbors = 0
	rowMainDiagonal = board.state[currentCell] + 1
	rowSecondaryDiagonal = board.state[currentCell] - 1

	for i in range(currentCell + 1, board.size):

		# Verify the same row
		if board.state[i] == board.state[currentCell]:
			neighbors += 1

		# Verify the main diagonal
		if rowMainDiagonal < board.size and board.state[i] == rowMainDiagonal:
			neighbors += 1

		rowMainDiagonal += 1

		# Verify the secondary diagonal
		if rowSecondaryDiagonal >= 0 and board.state[i] == rowSecondaryDiagonal:
			neighbors += 1

		rowSecondaryDiagonal -= 1

	return neighbors
