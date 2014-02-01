# !/usr/bin/python
# -*- coding: utf-8 -*-
import itertools

# magic ...
def new_word(chemin_str):
    # je passe une string car les tableau sont passé par reférence (pas de recursion possible, je pense)
    chemin = chemin_str.split(':')
    last_word = chemin[-1]

    # on genere toutes les possibilités de mots en switchant 1 lettre
    for i in xrange(0, len(last_word)):
        lettre = last_word[i]
        alphabet = [l for l in "abcdefghijklmnopqrstuvwxyz" if l != lettre]
        
        # on prend le début et la fin du mot sans la lettre
        prefix = last_word[:i]
        suffixe = last_word[i+1:]

        # ont créé les mot 
        possibilite = ["{}{}{}"%(prefix,l,suffixe) for l in alphabet]

        print possibilite
    print chemin


# Input
chemin = [raw_input("Entrez le mot de départ: ").lower(),]
arrivee = raw_input("Entrez le mot d'arrivée: ").lower()

if len(chemin[0]) != len(arrivee):
    print "Fail"
    quit()

# création du dico avec les mots de la bonne taille
dictionnaire = []
with open("dictionnaire.txt") as f:
    for line in f:
        mot = line.strip()

        if len(mot) == len(chemin[0]):
            dictionnaire.append(mot)

# on garde une trace de nos essais (doublon)
essais = []

# magic todo (désolé …)
if len(chemin) > 1:
    new_word(":".join(chemin)) 
else:
    new_word(chemin[0])

# test si on à trouver le bon chemin
if chemin[-1] == arrivee:
    for swap in chemin:
        print swap

######### code de fred ############
# Retourne si oui ou non le mot existe dans le dico
# def inDico(mot):
#     dico = open('dictionnaire.txt', 'r')

#     for line in dico:
#         if mot == dico:
#             return True

#     return False

# #
# # Fetch le prochain mot dans le chemin
# def fetchMot(depart, cible):
#     for i in range(len(depart)):
#         mot = list(depart)
#         mot[i] = list(cible)[i]
#         mot = "".join(mot)

#         if inDico(mot):
#             return mot
    
#     return False

# #           
# # Fonction principale
# def main():
#     continuer = True
#     chemin = []
#     i = 0

#     # Input
#     chemin.append(raw_input("Entrez le mot de départ: "))
#     arrivee = raw_input("Entrez le mot d'arrivée: ")
    
#     # Boucle de résolution
#     while continuer:
#         # On sort de la boucle si on a atteint le mot d'arrivee
#         if chemin[i] == arrivee:
#             continuer = False
        
#         # On fetch le prochain mot
#         resultatDico = fetchMot(chemin[i], arrivee)

#         # Si le dico nous retourne aucun mot, ben y'a pas de solution bro
#         if resultatDico == False:
#             continuer = False
#         else:
#             chemin.append(resultatDico)

#         i += 1
    
#     # Affichage des résultats
#     if chemin[i] == arrivee:
#         for line in chemin:
#             print line
#     else:
#         print("Aucune solution possible, SARRY")

# #main()
