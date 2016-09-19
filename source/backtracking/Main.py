from GenericObject import GenericObject
from itertools import permutations

def main():
	"""Main function"""

	print "************************************", "Zebra's Problem Solution", "************************************"

	# Inializating objects
	houseColors = GenericObject("HouseColors", ["vermelha", "amarela", "azul", "verde", "marfim"])
	housePositions = GenericObject("HousePositions", ["Esquerda1", "Esquerda2", "Meio", "Direita1", "Direita2"])
	nationalities = GenericObject("Nationalities", ["ingles", "espanhol", "noruegues", "ucraniano", "japones"])
	cigarretes = GenericObject("Cigarretes", ["Kool", "Chesterfield", "Winston", "Lucky_Strike", "Parliament"])
	drinks = GenericObject("Drinks", ["suco_de_laranja", "cha", "cafe", "leite", "agua"])
	pets = GenericObject("Pets", ["cachorro", "raposa", "caramujos", "cavalo", "zebra"])


	# All possible permutations for a list with length 5
	permutation = list(permutations(range(5)))

	# For each case of problem's solution, all the constraints must be checked, in order to find the right solution
	for houseColor in permutation:
		if houseColor[nationalities.components.index("ingles")] == houseColors.components.index("vermelha"):	# Constraint 1
			for pet in permutation:
				if pet[nationalities.components.index("espanhol")] == pets.components.index("cachorro"):	# Constraint 2
					for housePosition in permutation:
						if housePosition[nationalities.components.index("noruegues")] == housePositions.components.index("Esquerda1"):	# Constraint 3		
							for cigarrete in permutation:
								if cigarrete[houseColor.index(houseColors.components.index("amarela"))] == cigarretes.components.index("Kool"):	# Constraint 4
									if (housePosition[cigarrete.index(cigarretes.components.index("Chesterfield"))] - housePosition[pet.index(pets.components.index("raposa"))]) in (-1, 1):	# Constraint 5
										if (housePosition[houseColor.index(houseColors.components.index("azul"))] - housePosition[nationalities.components.index("noruegues")]) in (-1, 1):		# Constraint 6			
											if pet[cigarrete.index(cigarretes.components.index("Winston"))] == pets.components.index("caramujos"):	# Constraint 7
												for drink in permutation:
													if drink[cigarrete.index(cigarretes.components.index("Lucky_Strike"))] == drinks.components.index("suco_de_laranja"):	# Constraint 8
														if drink[nationalities.components.index("ucraniano")] == drinks.components.index("cha"):	# Constraint 9
															if cigarrete[nationalities.components.index("japones")] == cigarretes.components.index("Parliament"):	# Constraint 10
																if (housePosition[cigarrete.index(cigarretes.components.index("Kool"))] - housePosition[pet.index(pets.components.index("cavalo"))]) in (1, -1):	# Constraint 11
																	if drink[houseColor.index(houseColors.components.index("verde"))] == drinks.components.index("cafe"):	# Constraint 12
																		if (housePosition[houseColor.index(houseColors.components.index("verde"))] - housePosition[houseColor.index(houseColors.components.index("marfim"))]) == 1:	# Constraint 13
																			if housePosition[drink.index(drinks.components.index("leite"))] == housePositions.components.index("Meio"):	# Constraint 14
																				printSolution(nationalities, range(5))
																				printSolution(housePositions, housePosition)
																				printSolution(houseColors, houseColor)
																				printSolution(drinks, drink)
																				printSolution(cigarretes, cigarrete)
																				printSolution(pets, pet)
																				print


# Print the right solution for an object of class GenericObject
def printSolution(genericObj, answer):
	print "%14s: %17s%17s%17s%17s%17s" % (genericObj.typeObj, genericObj.components[answer[0]],
										    genericObj.components[answer[1]], genericObj.components[answer[2]],
										    genericObj.components[answer[3]], genericObj.components[answer[4]])
	

if __name__ == "__main__":
	main()