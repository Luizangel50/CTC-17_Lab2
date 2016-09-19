from math import exp

def function(values):
	"""Function especified on the problem"""

	x = values[0]
	y = values[1]

	return 	4*exp(-(pow(x, 2) + pow(y, 2))) + exp(-(pow(x - 5, 2) + pow(y - 5, 2))) + \
			exp(-(pow(x + 5, 2) + pow(y - 5, 2))) + exp(-(pow(x - 5, 2) + pow(y + 5, 2))) + \
		   	exp(-(pow(x + 5, 2) + pow(y + 5, 2)))

def adjustTemp(temperature, adjustParameter):
	"""Adjust the temperature's value with the adjust parameter"""

	return temperature*adjustParameter
	

def changeProbability(delta, temperature):
	"""Calculates the probability with a solution will be changed or not
	if delta is less or equal than 0"""

	return exp(delta/temperature)