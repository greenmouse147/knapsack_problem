from parser_me import parsefile

def check_si_objet_peut_etre_pris (objet) :
	#matrice de vétification
	verification = [0] * nbcont
	
	#pour chaque contraintes, on vérifie que l'objet entre dans toute les contraintes
	#on a que des 1 si ok
	for i in range(0,nbcont):
		#+2 car deux rangs de décalage pour atteindre les contraintes
		if contraintes[i] - objet[i+2] >=0 : verification[i] = 1
		else : break

		
	#Si on peut, on prend l'objet		
	if 0 not in verification : 
		return True
	else : return False

def ajouter_objet(objet) : 
	#print("ajout de l'objet") 
	for i in range(0,nbcont):
	#+2 car deux rangs de décalage pour atteindre les contraintes
		contraintes[i] -= objet[i+2]
	Z.append(objet)

def retirer_objet (objet):
	#print("retrait de l'objet") 
	for i in range(0,nbcont):
	#+2 car deux rangs de décalage pour atteindre les contraintes
		contraintes[i] += objet[i+2]
		Z.remove(objet)

def check_et_ajout_objet (objet): 
	if check_si_objet_peut_etre_pris(objet) == True : 
		ajouter_objet(objet)
		return True
	else : return False

def optimisation (): 
	#cao = contrainte à optimiser
	#regarder la contante ou il y a le moins de place : 
	cao_rang = contraintes.index(min(contraintes))
	cao_val = contraintes(cao_rang)
	
	
#=======================================#

##definition des variables globales		
global nbobjet, nbcont, contraintes, objets
#nbobjet, nbcont, contraintes, objets = parsefile("Jeux_de_Donnees/n500m30_21.dat",addid=True)
nbobjet, nbcont, contraintes, objets = parsefile("Jeux_de_Donnees/n100m5_1.dat",addid=True)
#Structure objet :
	#[id, Valeur, c1, ..... cn, Rendement]

#objets_retenus
global Z 
Z = []
#Matrice de resultats
#Par défaut on ne prend pas d'objet et on met à 1 les objets que l'on prend
global res
res = [0] * nbobjet

#=======================================#

#Calcul de la valeur
for i in objets : 
	v = i[1] / (sum(i[2:])) 
	i.append(v)

#Classer les resultats par valeurs
objets_sorted = sorted(objets,key=lambda l:l[-1], reverse = True)
#print(objets_sorted)

for objet in objets_sorted :
	check_et_ajout_objet(objet)

#Calcul de la valeur de la solution
valsolution = 0
for elem in Z :
	valsolution += elem[1]



#=======================================#


##Affichage desrangs des objets
#print("objets classés : ")
#for elem in objets_sorted:
#	print(elem)

print("\n\n\n")		
#mise en forme des resultats
print("Objets retenus: ")
for elem in Z:
	print(elem)

for elem in Z: 
	#print(X.index(elem))
	res[objets.index(elem)] = 1

print("Matrice des objets pris : ",res)

print("valeur de la solution initiale : ",valsolution)
print("Capacité restante :")
print(contraintes)
print("\nOptimisation :")
optimisation()