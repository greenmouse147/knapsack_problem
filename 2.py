from parser_me import parsefile

#nbval, nbcont, contraintes, objets = parsefile("Jeux_de_Donnees/n100m5_1.dat",addid=True)
nbobjet, nbcont, contraintes, objets = parsefile("Jeux_de_Donnees/n500m30_21.dat",addid=True)

#objets_retenus
Z = []
#Matrice de resultats
#Par défaut on ne prend pas d'objet et on met à 1 les objets que l'on prend
res=[0] * nbobjet
#Calcul de la valeur
for i in objets : 
	v = i[1] / (sum(i[2:])) 
	i.append(v)
	

#Classer les resultats par valeurs
objets_sorted = sorted(objets,key=lambda l:l[-1], reverse = True)
#print(objets_sorted)

#Vérifier si on peut prendre l'objet dans le sac
for objet in objets_sorted :
	verification = [0] * nbcont 
	for i in range(0,nbcont):
		#+2 car deux rangs de décalage pour atteindre les contraintes
		if contraintes[i] - objet[i+2] >=0 : verification[i] = 1
		else : break

#Si on peut, on prend l'objet		
	if 0 not in verification : 
		#print("ajout de l'objet") 
		for i in range(0,nbcont):
		#+2 car deux rangs de décalage pour atteindre les contraintes
			contraintes[i] -= objet[i+2]
		Z.append(objet)

		

print("Objets retenus: ")
for elem in Z:
	print(elem)





#mise en forme des resultats
for elem in Z: 
	#print(X.index(elem))
	res[objets.index(elem)] = 1

print("Matrice des objets pris : ",res)



print("Capacité restante :")
print(contraintes)
print("\n")