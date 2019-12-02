#coding: utf-8
#ere x3

n = int(input("taille max de liste \n"))

def creation_liste(n):
    i = 2
    liste = []
    while i <= n:
        liste.append(i)
        i += 1
    return (liste)

#liste donne les non multiple de div
def liste_non_multiple(div, liste):
    lnm = []
#for permet de cree une liste ou liste % div diff de 0 = lnm
    for i in range(len(liste)):
        if liste[i] % div != 0:
            lnm.append(liste[i])
    return (lnm)

def eratosthene(x):
    entiers = creation_liste(x)
    premier = []
    while entiers:
        premier.append(entiers[0])
        entiers = liste_non_multiple(entiers[0], entiers)
    return (premier)

def liste_facteurs_premiers(n):
    premier = eratosthene(n)
    facteur = []
    i = 0
    while i < len(premier):
        if n % premier[i] == 0:
            facteur.append(premier[i])
        i += 1
    return (facteur)

print(liste_facteurs_premiers(n))