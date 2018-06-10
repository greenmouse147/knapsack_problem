from parser_me import parsefile


def check_si_objet_peut_etre_pris (objet,temp_contraintes=[]) :
	if temp_contraintes == [] :
		global contraintes
		temp_contraintes=list(contraintes)
		
	#matrice de vétification
	verification = [0] * nbcont
	
	#pour chaque contraintes, on vérifie que l'objet entre dans toute les contraintes
	#on a que des 1 si ok
	for i in range(0,nbcont):
		#+2 car deux rangs de décalage pour atteindre les contraintes
		if temp_contraintes[i] - objet[i+2] >=0 : verification[i] = 1
		else : break

		
	#Si on peut, on prend l'objet		
	if 0 not in verification : 
		return True
	else : return False

def ajouter_objet(objet) : 
	global contraintes
	global objets_retenus
	
	#print("ajout de l'objet") 
	for i in range(0,nbcont):
	#+2 car deux rangs de décalage pour atteindre les contraintes
		contraintes[i] -= objet[i+2]
	objets_retenus.append(objet)

def retirer_objet (objet):
	global contraintes
	global objets_retenus
	#print("retrait de l'objet") 
	for i in range(0,nbcont):
	#+2 car deux rangs de décalage pour atteindre les contraintes
		contraintes[i] += objet[i+2]
	objets_retenus.remove(objet)

def check_et_ajout_objet (objet): 
	if check_si_objet_peut_etre_pris(objet) == True : 
		ajouter_objet(objet)
		return True
	else : return False

def fusion_objet_temp (liste_objet_a_ajouter) : 
	#créer un objet temp pour fusioner les objets
	temp_objet = [0] * (nbcont + 2)
	temp_objet.insert(0,"tempid")
	
	for objet in liste_objet_a_ajouter :
		for i in range (1,nbcont+3):#+2 pour valeur et rendement
			temp_objet[i] += objet[i]
	
	return temp_objet
	
def check_une_contrainte (objet_initial,objet_de_remplacement,index_contrainte) :
	if objet_initial[index_contrainte] <= objet_de_remplacement[index_contrainte] : 
		return True
	else : return False

def check_remplacement (objet_initial,objet_de_remplacement) : 
	
	global contraintes
	replace = False
	#si on a un meilleur rendement, et une meilleure valeur on enlève l'objet initial de la liste (calculs plus simples)
	if check_une_contrainte(objet_initial,objet_de_remplacement,-1) == True and check_une_contrainte(objet_initial,objet_de_remplacement,1) == True :
	
		#création d'un objet de contrainte contenant les valeurs des contraintes après avoir retiré un objet
		temp_contraintes = list(contraintes) 	
		#print(contraintes)
		for i in range(0,nbcont):
		#+2 car deux rangs de décalage pour atteindre les contraintes
			temp_contraintes[i] += objet_initial[i+2]
		
		#print(contraintes)
		#print(temp_contraintes)
		#input()
		##retirer_objet(objet_initial)
		#on regarde si notre objet temporaire (fusion de deux objets) peut être pris
		if check_si_objet_peut_etre_pris(objet_de_remplacement,temp_contraintes) == True : 
			replace = True
		#on remet la liste dans son etat initial
		#ajouter_objet(objet_initial)
	return replace

def remplacer(objet_a_remplacer,liste_objet_remplacement):
		retirer_objet(objet_a_remplacer)
		for elem in liste_objet_remplacement :
			ajouter_objet(elem)
		
def optimisation (): 
	#cao = contrainte à optimiser
	#regarder la contante ou il y a le moins de place : 
	#cao_rang = contraintes.index(min(contraintes))
	#cao_val = contraintes(cao_rang)
	
	#tempon des objets retenus (utilisé pour la boucle)
	global objets_retenus
	global objets_non_retenus
	temp_objets_retenus = []
	temp_objets_retenus = list(objets_retenus)
	#debug
	"""
	print("objets que nous allons traiter : ")
	for elem in temp_objets_retenus : 
		print(elem)
	"""
	for objet_initial in temp_objets_retenus :
		#debug
		"""
		print("objets que nous allons traiter : ")
		for elem in temp_objets_retenus : 
			print(elem)
		
		
		print("objet en cours de traitement : " + str(objet_initial))
		"""
		#on crée la liste des remplacants
		remplacants_potentiels = [[0,0,0]]
		#on parcourt les couples d'objets possibles 
		for i in range (0,len(objets_non_retenus)):
			for j in range (0,len(objets_non_retenus)):
				if i != j :
					temp_objet = fusion_objet_temp([objets_non_retenus[i],objets_non_retenus[j]])
					replace = check_remplacement(objet_initial,temp_objet)
					#print(replace)
					
					
					
					#si le couple est meilleur, on note le couple dans la liste des remplacants_potentiels)
					if replace == True :
					
						#print("objet 1 : " + str(objets_non_retenus[i]))
						#print("objet 2 : " + str(objets_non_retenus[j]))
						#print("fusion  : " + str(temp_objet))
						#print("objet i : " + str(objet_initial))
						#input()

						#on garde le couple et la valeur ajoutée
						valeur_ajoutee = (objets_non_retenus[i][1] + objets_non_retenus[j][1]) - (objet_initial[1])
						remplacants_potentiels.append([i,j,valeur_ajoutee])
		
		remplacants_potentiels_sorted = list(sorted(remplacants_potentiels,key=lambda l:l[2], reverse = True))
		#si il y a des remplacants potentiels
		if remplacants_potentiels_sorted[0] != [0,0,0] :
			#debug
			"""
			print("\n\n\n\n")
			
			print ("objet retenu1 " + str(objets_non_retenus[remplacants_potentiels_sorted[0][0]]))
			print ("objet retenu2 " + str(objets_non_retenus[remplacants_potentiels_sorted[0][1]]))
			"""
			remplacer(objet_initial,
			[
				objets_non_retenus[remplacants_potentiels_sorted[0][0]],
				objets_non_retenus[remplacants_potentiels_sorted[0][1]]
			]
			)
			
			
			#maj objets non retenus
			objets_non_retenus = [value for value in objets if value not in objets_retenus]
			
			"""
			#debug
			print("remplacants")
			for i in range (0,len(remplacants_potentiels_sorted)%10)  : 
				print(remplacants_potentiels_sorted[i])			
			print("\n\n\n objets retenus")
			for elem in temp_objets_retenus : 
				print(elem)			
			print("\n\n\n objets non retenus")
			for elem in objets_non_retenus : 
				print(elem)
			
			print("\n\n\n objets retenus après remplacement")
			for elem in objets_retenus : 
				print(elem)
			"""
		
		else : #debug
			"""
			print("pas de remplacants corrrects")	
			"""
			pass

#=======================================#

##definition des variables globales		
global nbobjet, nbcont, contraintes, objets
nbobjet, nbcont, contraintes, objets = parsefile("Jeux_de_Donnees/n100m5_1.dat",addid=True)
#debug
"""
for elem in objets :
	print(elem)
	input()
"""
#nbobjet, nbcont, contraintes, objets = parsefile("Jeux_de_Donnees/n100m5_1.dat",addid=True)
#Structure objet :
	#[id, Valeur, c1, ..... cn, Rendement]

#objets_retenus
global objets_retenus 
objets_retenus = []
global objets_non_retenus
objets_non_retenus = []
#Matrice de resultats
#Par défaut on ne prend pas d'objet et on met à 1 les objets que l'on prend
global res
res = [0] * nbobjet

global res_optim
res_optim = [0] * nbobjet

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
for elem in objets_retenus :
	valsolution += elem[1]

objets_non_retenus = [value for value in objets if value not in objets_retenus]

#=======================================#

##Affichage des resultats avant optimisation

#mise en forme des resultats


print("Objets retenus initalements: ")
for elem in objets_retenus:
	print(elem)


#mise en forme de la matrice de resultats
for elem in objets_retenus: 
	res[objets.index(elem)] = 1


print("Matrice des objets pris : ",res)
print("valeur de la solution initiale : ",valsolution)
print("Capacité restante :")
print(contraintes)
#input("test")

print("\n\n\nOptimisation :")
optimisation()

print("Objets retenus après optimisation: ")
for elem in objets_retenus:
	print(elem)

#mise en forme de la matrice de resultats
for elem in objets_retenus:
	#print(elem) 
	res_optim[objets.index(elem)] = 1


print("Matrice des objets pris : ",res_optim)

#Calcul de la valeur de la solution
valsolution = 0
for elem in objets_retenus :
	valsolution += elem[1]
print("valeur de la solution initiale : ",valsolution)
print("Capacité restante :")
print(contraintes)

#for elem in objets:
#	print(objets)