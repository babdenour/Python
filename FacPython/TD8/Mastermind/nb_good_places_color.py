#coding: utf-8

def nb_bien_places_couleur(proposition, solution, couleur):
    i = 0;
    nbpc = 0;
    while (i < len(proposition)):
        if (proposition[i] == solution[i] and couleur == proposition[i]):
            nbpc += 1;
        i += 1;
    return (nbpc);