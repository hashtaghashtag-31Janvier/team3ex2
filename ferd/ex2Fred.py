# !/usr/bin/python
# -*- coding: utf-8 -*-

#
# Retourne si oui ou non le mot existe dans le dico
def inDico(mot):
	dico = open('dictionnaire.txt', 'r')

	for line in dico:
		if mot == dico:
			return True

	return False

#
# Fetch le prochain mot dans le chemin
def fetchMot(depart, cible):
	for i in range(len(depart)):
		mot = list(depart)
		mot[i] = list(cible)[i]
		mot = "".join(mot)

		if inDico(mot):
			return mot
	
	return False

#			
# Fonction principale
def main():
	continuer = True
	chemin = []
	i = 0

	# Input
	chemin.append(raw_input("Entrez le mot de départ: "))
	arrivee = raw_input("Entrez le mot d'arrivée: ")
	
	# Boucle de résolution
	while continuer:
		# On sort de la boucle si on a atteint le mot d'arrivee
		if chemin[i] == arrivee:
			continuer = False
		
		# On fetch le prochain mot
		resultatDico = fetchMot(chemin[i], arrivee)

		# Si le dico nous retourne aucun mot, ben y'a pas de solution bro
		if resultatDico == False:
			continuer = False
		else:
			chemin.append(resultatDico)

		i += 1
	
	# Affichage des résultats
	if chemin[i] == arrivee:
		for line in chemin:
			print line
	else:
		print("Aucune solution possible, SARRY")

main()
