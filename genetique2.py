#codding : utf-8
from parser_me import parsefile
import random

global nbobjet, nbcont, contraintes, objets
nbobjet, nbcont, contraintes, objets = parsefile("Jeux_de_Donnees/n100m5_1.dat",addid=True)
#print(objets)
#Constantes 
#contrainte initiale
global _CONTRAINTES_INITIALES
_CONTRAINTES_INITIALES = list(contraintes)

#debug vars
global nbviable
nbviable=0

def generate(nbobjet,popSize):
	pop = [[[random.randint(0,1) for i in range(nbobjet)]] for j in range(popSize)]
	#print pop
	return pop

def check_viability(solution) : 

	viable = True
		
	for i in range (0,len(solution[1])) : 
		if solution[1][i] > _CONTRAINTES_INITIALES[i] :
			viable = False
			break
	
	return viable

def calculate_weight(solution) :
	#definition des variables 
	valeur_solution = 0
	weight_solution = [0] * nbcont
	
	#calcul de poids de la solution
	for i in range (0,len(solution[0])):
		
		if solution[0][i] == 1 :
			#input(":)")
			for j in range (len(weight_solution)) : 
				weight_solution[j] += objets[i][j+2]
	
	#on ajoute le poids de la solution ou le met à jour
	try  : 
		solution[1] = weight_solution
	except IndexError: 
		solution.append(weight_solution)
		
	#calcul de la valeur de la solution 
	for i in range (0,len(solution[0])):
		if solution[0][i] == 1 :
			valeur_solution += objets[i][1]
	
	try : 
		solution[2] = valeur_solution
	except IndexError :
		solution.append(valeur_solution)
		
def repair_solution(solution) : 
	#global nbviable #debug 

	#calcul du poids et de la valeur de la solution 
	calculate_weight(solution)
	
	#print(_CONTRAINTES_INITIALES)
	#print(solution)
	#input()
	
	#si la solution  n'est pas viable, enlever des objets de droite à gauche
	while check_viability(solution) == False : 
		#print("solution non viable : " + str(solution))
		for i in reversed(range(len(solution[0]))) :
			if solution[0][i] == 1 : 
				solution[0][i] = 0
				calculate_weight(solution)
				break
	#print("solution viable     : " + str(solution))
	
	
	return solution

	
#générer la population initiale	
pop = generate(nbobjet,50)

#debug
"""
for elem in pop :
	print(elem)
"""
#vérifier la population initiale

for elem in pop :
	#print(elem)
	repair_solution(elem)

#debug
"""
print(_CONTRAINTES_INITIALES)
for elem in pop :
	print(check_viability(elem))
	print(elem)
"""
	
#séléctionner l'élite
	##classement des solutions
pop = list(sorted(pop,key=lambda l:l[2], reverse = True))

parents=list(pop[0:10])

#selectionner les chanceux
for i in range (0,10):	
	parents.append( pop[random.randint(10,len(pop)-1)] )

for elem in parents : 
	print(elem)
print(len(parents))
#Créer les enfants

#Vérifier les enfants

#remplacer les plus faibles de la population

#recommencer