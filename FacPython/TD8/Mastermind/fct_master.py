#coding: utf-8
import random;

def generation_solution():
    liste = [];
    i = 0;
    while (i < 5):
        liste.append(random.randint(0, 7));
        i += 1;
    return (liste);
    

def min_int(x, y):
    if (x > y):
        return (x);
    else :
        return (y);

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
        nb_occ[k] += 1;
    print("\n\tLe nombre d'occurence: ", nb_occ);
    return (nb_occ);

def nb_bien_places_couleur(proposition, solution, couleur):
    i = 0;
    nbpc = 0;
    while (i < len(proposition)):
        if (proposition[i] == solution[i] and couleur == proposition[i]):
            nbpc += 1;
        i += 1;
    return (nbpc);

def nb_couleurs_mal_placees(combi, sol):
    i = 0;
    j = 0;
    nbcmp = 0;
    while (i < len(combi)):
        if (combi[i] != sol[i]):
            for j in combi[j]:
                j += 1;
            print(j);
            nbcmp += 1;
        i += 1;
    return (nbcmp);