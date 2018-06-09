
#id largeur, hauteur, prix
X = [
	[1,4,7,8],
	[2,3,4,4],
	[3,5,5,7],
	[4,3,4,5],
	[5,2,3,2]
]

#constraint 
Y = [13,16]

#resultats
Z = []

#Calcul de la valeur
for i in X : 
	v = i[3] / (i[1]+i[2]) 
	i.append(v)
	

#Classer les resultats par valeurs
X_sorted = sorted(X,key=lambda l:l[4], reverse = True)


#res = [0] * 5
#res = [0] * 5
for j in X_sorted : 
	if Y[0] - j[1] >= 0 and Y[1] - j[2] >=0 : 
		Y[0]-=j[1]
		Y[1]-=j[2]
		Z.append(j)
		#res[j[0]] = 1
		

print("Objets retenus: ")
print(Z)

#####
#Par défaut on ne prend pas d'objet et on met à 1 les objets que l'on prend
res = [0] * 5
for elem in Z: 
	#print(X.index(elem))
	res[X.index(elem)] = 1
print("Matrice des objets pris : ",res)



print("Capacité restante :")
print(Y)
print("\n")



