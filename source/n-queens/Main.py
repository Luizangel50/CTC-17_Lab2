import Board
from Helper import calculateCost, calculateNeighbors
from time import time
from copy import copy, deepcopy
from random import randint


# Array with board's sizes
SIZES_BOARD = [10, 15, 20, 25]

def main():
	"""Main function"""

	# For each board's size, execute the Hill Climbing Algorithm,
	# print the final state, the final cost of the final state and the execution time
	for size in SIZES_BOARD:

		print "*************************", size, "X", size, "BOARD", "*************************"
		board = Board.Board(size)

		initialTime = time()
		hillClimbingSearch(board)
		finalTime = time() - initialTime

		print "Final state:", board.state
		print "Final cost:", calculateCost(board)
		print "Execution time:", finalTime
		print


def hillClimbingSearch(board):
	"""Function that implements the Hill Climbing algorithm with some modification"""

	newBoard = modifyState(board)
	newCost = calculateCost(newBoard)

	# If new cost is 0, return
	if newCost == 0:
		board.state = list(newBoard.state)
		return

	# But if the new cost is equal to current cost,
	# get a random state to avoid local maximum
	elif newCost == calculateCost(board):
		randomStateChange(board)

	# Otherwise, the new cost is less than the current's cost
	else:
		board.state = list(newBoard.state)


	# Call Hill Climbing Algorithm recursively
	hillClimbingSearch(board)


def modifyState(board):
	"""Calculates if the board might change its state or not based on the
	cost of a possible new state"""

	# For now, the minimun cost is the current cost
	minimumCost = calculateCost(board)

	# Pick a copy of the board
	newBoard = deepcopy(board)

	# For each i column
	for i in range(0, board.size):

		# for each j row
		for j in range(0, board.size):

			# Old value of the row
			oldValue = newBoard.state[i]

			# Change that value to j
			newBoard.state[i] = j

			# Calculate the new board's cost
			newCost = calculateCost(newBoard)

			# If the new cost is less than the current minimum,
			# change the value of minimumCost
			if newCost < minimumCost:
				minimumCost = newCost

			# Otherwise, remains the old value
			else:
				newBoard.state[i] = oldValue

	return newBoard

def randomStateChange(board):
	"""Select a random row for a queen located on a random column for change its position
	to a different row, but remaining on the same column"""

	# Select a random column and a random row
	randomColumn = randint(0, board.size-1)
	randomRow = randint(0, board.size-1)

	# While the random row is equal to queen's position 
	# on the random column, find another random row
	while randomRow == board.state[randomColumn]:
		randomRow = randint(0, board.size-1)

	board.state[randomColumn] = randomRow

if __name__ == "__main__":
	main()