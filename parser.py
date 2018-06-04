#!/usr/bin/env python
#-*- coding: utf-8 -*-
import csv, struct

#with open('Jeux_de_Donnees/n100m30_1.dat', 'r') as csvfile:
with open('n100m5_1.dat', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ')
	init = reader.__next__()
	init[:] = [int(item) for item in init if item != '']
	##print(init)
	
	nbval = init[0]
	nbconst = init[1]
	objets = []
	for i in range (0,nbval):
		objets.append([None]*(nbconst+1))
	
	#remplissage valeur objet
	j=0
	for i in range(0,nbval//10) :
		row = reader.__next__()
		row[:] = [int(item) for item in row if item != '']
		
		##print(row) 
		for item in row :
			objets[j][0] = item			
			j+=1		
	#print(objets)
	
	#ignorer ligne separation
	row = reader.__next__()
	
	#récupèration des contraintes
	contrainte=[]
	if nbconst < 10 : nbligneconst = 1
	else : nbligneconst = nbconst // 10 
	print(nbligneconst)
	for l in range(0,nbligneconst):
		contraintetemp = reader.__next__()
		contrainte[:] += [int(item) for item in contraintetemp if item != '']
	print(contrainte)

	#remplissage des contrainte
	for k in range(1,nbconst+1) :
		#ignorer ligne separation
		row = reader.__next__()
		j=0
		
		for i in range(0,nbval//10) :
			row = reader.__next__()
			row[:] = [int(item) for item in row if item != '']
			##print(row) 
			for item in row :
				#print(k)
				#print(j)
				
				
				objets[j][k] = item	
				j+=1	

	print(objets)
	"""		
	for row in reader :
		row[:] =  [int(item) for item in row if item != '']
		for item in row : 
			objets[indice[0]] = item 
			indice +=1
		if indice == 
			
"""