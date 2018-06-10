#codding : utf-8

class individu : 
	"""
		cette class permet de créer une solution appelée ici individu
	"""
	def __init__(self, id) :
		self.id = id
		self.objets = []
		self.valeur = 0
	
	def add_objet(self,obj) : 
		self.objets.append(obj) 
	
	def remove_objet(self, obj) :
		self.objets.remove(obj)
	
	def make_child(solution1, solution2):
		individu(3)
		
	

class objets : 
	"""
		Cette classe crée un objet
	"""
	def __init__(self,id, valeur, contraintes) : 
		self.id = id
		self.valeur = valeur
		self.contraintes = contraintes
		#reprendre constructif calcul
		#self.rendement = 
		

solution1 = individu(1)	
solution2 = individu(2)	
print(solution1.id)

"""add objets"""
#solution1.add_objet(53)
#solution1.add_objet(43)
#solution1.add_objet(45)
#print(solution1.objets[0])

solution3= individu.make_child(solution1,solution2)
print(solution3)