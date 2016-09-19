from time import time
from SimulatedAnnealing import simulatedAnnealing

# The minimum temperature for simulated annealing algorithm
MINIMUM_TEMPERATURE = 0.00001
ADJUST_PARAMETER = 0.95

def main():
	"""Main function"""

	print "**********************", "Simulated Annealing", "**********************"
	print "Calculating maximum value of a function"

	# Initial solution
	solution = [20, -20]

	initialTime = time()

	# Execute the algorithm
	maximum = simulatedAnnealing(solution, MINIMUM_TEMPERATURE, ADJUST_PARAMETER)
	finalTime = time() - initialTime

	print "Maximum value: ", maximum
	print "Execution time: ", finalTime 
	

if __name__ == "__main__":
	main()