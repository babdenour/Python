#coding: utf-8
import random;

def generation_solution():
    liste = [];
    i = 0;
    while (i < 5):
        liste.append(random.randint(0, 7));
        i += 1;
    print("\n\tlist generation = ", liste);
    return (liste);
    

def min_int(x, y):
    
    if (x > y):
        return (x);
    else :
        return (y);

def nb_bien_places_couleur(proposition, solution, couleur):
    
    i = 0;
    nbpc = 0;
    while (i < len(proposition)):
        if (proposition[i] == solution[i] and couleur == proposition[i]):
            nbpc += 1;
        i += 1;
    return (nbpc);

def nb_bien_places(proposition, solution):

    i = 0;
    npbp = 0;
    while (i < len(proposition)):
        if (proposition[i] == solution[i]):
            npbp += 1;
        i += 1;
    return (npbp);

def compte_occurences(liste):
    
    i = 0;
    nb_occ = [0, 0, 0, 0, 0, 0, 0, 0];
    for i in range (len(liste)):
        k = liste[i];
        nb_occ[k] = nb_occ[k] + 1;
    print("\n\tLe nombre d'occurence: ", nb_occ);
    return (nb_occ);

liste = generation_solution();
print(liste);
compte_occurences(liste);
print(liste);