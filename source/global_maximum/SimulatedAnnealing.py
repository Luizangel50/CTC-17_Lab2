from sys import float_info
from Helpers import function, adjustTemp, changeProbability
from random import random

def simulatedAnnealing(solution, minimumTemperature, adjustParameter):
	"""Function that implements the Simulated Anneling algorithm for the function of the problem"""

	# Initialize maximum as the minor float
	maximum = float_info.min

	# For each i between -50 and 50
	for i in range (-50, 50):

		# For each j between -50 and 50
		for j in range (-50, 50):

			# Set initial temperature as 1
			temperature = 1

			# Change solution's values based on i and j
			currentSolution = [solution[0] + i, solution[1] + j]
			currentValue = function(currentSolution)

			# Update maximum point, if necessary
			if maximum < currentValue:
				maximum = currentValue

			# While temperature is higher than MINIMUM_TEMPERATURE
			while temperature > minimumTemperature:

				# Adjust temperature
				temperature = adjustTemp(temperature, adjustParameter)

				# Sum a random value between (0, 1) for X and Y of the current solution
				newXValue = currentSolution[0] + random()
				newYValue = currentSolution[1] + random()

				newValue = function([newXValue, newYValue])

				# Difference between the old value and the new value
				delta = currentValue - newValue

				# If delta > 0, current solution is the new one
				if delta > 0:
					currentSolution = [newXValue, newYValue]

					# Update maximum point, if necessary
					if maximum < newValue:
						maximum = newValue

				# Otherwise
				elif delta <= 0:

					# Only change the current solution with a probability
					# based on delta and current temperature
					probability = changeProbability(delta, temperature)

					if probability > random():
						currentSolution = [newXValue, newYValue]

						# Update maximum if necessary
						if maximum < newValue:
							maximum = newValue


	return maximum