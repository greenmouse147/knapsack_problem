#coding : utf-8

from parser_me import parsefile
import random
import time
import matplotlib.pyplot as plt

start_time = time.time()

global nbobjet, nbcont, contraintes, objets
nbobjet, nbcont, contraintes, objets = parsefile("Jeux_de_Donnees/n100m5_1.dat",addid=True)
#print(objets)
#Constantes 
#contrainte initiale

global _CONTRAINTES_INITIALES
_CONTRAINTES_INITIALES = list(contraintes)

#debug vars
#global nbviable
#nbviable=0

def generate(nbobjet,popSize):
	pop = [[[random.randint(0,1) for i in range(nbobjet)]] for j in range(popSize)]
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
	
def recalculate_weight(solution,added_object, action="add"):
	
	if action == "add" : 
		#calcul de poids de la solution
		for j in range (len(solution[1])) : 
			solution[1][j] += objets[added_object][j+2]
						
		#calcul de la valeur de la solution 
		solution[2] += objets[added_object][1]
	
	elif action == "remove" :
		#calcul de poids de la solution
		for j in range (len(solution[1])) : 
			solution[1][j] -= objets[added_object][j+2]
						
		#calcul de la valeur de la solution 
		solution[2] -= objets[added_object][1]

def repair_solution(solution) : 
	#global nbviable #debug 

	#calcul du poids et de la valeur de la solution 
	calculate_weight(solution)
	#print("\n\n\n")
	#print(solution)
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
	
	
	#amélioration de la solution
	#on ajoute l'objet 
	i = random.randint(0,len(solution) -1)
	
	if solution[0][i] == 0 : 
		solution[0][i] = 1
		#on recalcule la solution
		recalculate_weight(solution,i,action="add")
	#si la solution est toujours viable, on garde, sinon on annule
	if check_viability(solution) == False : 
			solution[0][i] = 0
			recalculate_weight(solution,i,action="remove")
	
	
	return solution

def make_children(parents,childrens) :
	#selectoner parents random
	parent1 = parents.pop(random.randint(0,len(parents)-1))
	parent2 = parents.pop(random.randint(0,len(parents)-1))
	
	#print("parent 1" + str(parent1))
	#print("parent 2" + str(parent2))
	
	#selectionner le père partie droite 
	father = random.randint(0,1)
	 
	
	#déclaration de l'enfant
	children = [[]]
	
	#création de l'enfant moitier père, moitier mère
	if father == 0 :
		children[0] = list(parent1[0][0:((len(parent1[0])//2))])
		children[0].extend(list(parent2[0][((len(parent2[0])//2)):]))
	elif father == 1: 
		children[0] = list(parent2[0][0:((len(parent1[0])//2))])
		children[0].extend(list(parent1[0][((len(parent2[0])//2)):]))
	else : 
		input("Erreur")
	#debug
	"""
	#print("enfant 1" + str(children))
	#print(len(children[0]))
	#print(len(parent1[0]))
	"""
	
	#mutation aléatoire
	for i in range(0,2) : 
		already_exist = 1 
		while already_exist == 1  : 
			already_exist = 0 #0=false
			
			rand_mut = random.randint(0,(len(children[0])-1))
			#print(rand_mut)
			if children[0][rand_mut] == 0 : 
				children[0][rand_mut] =1
			else : children[0][rand_mut] = 0
			
			for elem in pop :
				if elem[0] == children[0] : 
					already_exist = 1
					break
	
	childrens.append(children)

def make_children_2(parents,childrens):
	"""
	Takes 2 binary lists and with probablity pX performs uniform crossover at probability pU to produce a list of 2 new binary lists.
	"""
	#selectoner parents random
	parentA = parents.pop(random.randint(0,len(parents)-1))
	parentB = parents.pop(random.randint(0,len(parents)-1))

	childA = parentA[:]
	childB = parentB[:]
	#print(childA)
	if 1 > random.random():
		for i in range(len(parentA[0])):
			if (random.randint(0,1000)%1) == 1:
				childA[0][i] = parentB[0][i]
				childB[0][i] = parentA[0][i]
	
	childrens.append(childA)
	childrens.append(childB)
	
max_generations = 10000
max_time = 10
P = 50 # Population size
E = 6 # number of Elites
C = 4 # lucky guys


#input("Cliquez sur 'Enter' pour lancer le programme (1minute)")
#générer la population initiale
pop = generate(nbobjet,P)

#compteur de génération 
z = 0
#data
Generation = []
Results = []
print("Calcul genetique : "+ str(max_time/60) +" minute. Veuillez patienter..", flush=True)
while 1 : 
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
		#selection des élites
	parents=list(pop[0:E])
	#print(len(pop))
		#selectionner les chanceux
	for i in range (0,C):
		parents.append(pop[random.randint(E,(len(pop)-1))] )

	"""
	for elem in parents :
		print(elem)
	print(len(parents))
	"""

	#Créer les enfants
	childrens=[]
	while len(parents) != 0 :
		make_children(parents,childrens)

	#Vérifier les enfants
	for elem in childrens :
		#print(elem)
		repair_solution(elem)

	#remplacer les plus faibles de la population
		##ajouter les enfants à la population
	for elem in childrens :
		pop.append(elem)

		#classer la nouvelle population
	pop = list(sorted(pop,key=lambda l:l[2], reverse = True))
	#depop
	POPme = (C + E)/2
	#POPme = (C + E) #if 2 child created 'make_child_2'
	pop = list(pop[0:-int(POPme)])

	#add data to graph
	Generation.append(z)
	Results.append(pop[0][2])
	if (time.time() - start_time) > max_time - 1  : 
		break
	
	z+=1

	

print("génération ; taille : " + str(len(pop)),flush=True)
print("Valeur de la meilleure solution :" + str(pop[0][2]),flush=True)
print("Meilleure solution :" + str(pop[0][0]),flush=True)
print("Contraintes de la solution" + str(pop[0][1]), flush=True)

print("Temps d execution : %s secondes ---" % (time.time() - start_time))
input("Cliquez sur 'enter' pour afficher la courbe des resultats:")
#evolution des solutions

plt.plot(Generation, Results)
plt.show()