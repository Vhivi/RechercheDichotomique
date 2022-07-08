#!/usr/bin/python
# -*- coding: utf-8 -*-

# Projet de recherche dichotomique

# Pour vous introduire à la complexité algorithmique, vous pouvez créer un
# algorithme simple de recherche dichotomique.

# Vous utiliserez un tableau trié et diviserez le tableau à chaque itération.
# Si le nombre désiré est dans la première partie, vous continuez avec la
# première moitié du tableau et rejetez la seconde. Ensuite divisez la première
# moitié en 2 et répétez l’operation jusqu’à trouver le nombre voulu.

import random


def rechercheDichotomique(valeur, tableautrilist):
    # Taille du tableau
    tailletableau = len(tableautrilist)
    # Vérification si le tableau n'est pas vide
    if tailletableau == 0:
        return print('Le tableau est vide')
    
    # Si le tableau ne contient qu'une valeur et qu'elle n'est pas recherchée
    if tailletableau == 1 and valeur != tableautrilist[0]:
        return print('La valeur recherchée {} n\'existe pas dans le tableau.'
                     .format(valeur))
    
    # Trouver la position centrale du tableau
    positioncentrale = round(tailletableau / 2)
    
    # Comparaison de la valeur recherchée avec la position centrale
    # Si la valeur est égale, on retourne
    if valeur == tableautrilist[positioncentrale]:
        return print('La valeur recherchée {} a été trouvée dans le tableau.'
                     .format(valeur))
    # Si la valeur est inférieure, on reprend la fonction avec la partie
    # inférieure du tableau
    elif valeur < tableautrilist[positioncentrale]:
        rechercheDichotomique(valeur, tableautrilist[0:positioncentrale])
    # Sinon
    else:
        rechercheDichotomique(valeur, tableautrilist[positioncentrale:tailletableau])


def main():
    # Création d'un tableau
    tableaulist = []
    # Limitation maximum de la taille du tableau
    tableaulen = random.randint(1, 5000)
    # Remplissage aléatoire du tableau
    for i in range(0, tableaulen):
        tableaulist.append(random.randint(0,i))
    
    # Triage du tableau
    tableautrilist = sorted(tableaulist)
    
    # Demande de la valeur recherchée
    valeur = int(input('Quelle valeur recherchez-vous ?'))
    
    # Appel de la recherche puis afficher le résultat
    rechercheDichotomique(valeur, tableautrilist)

main()