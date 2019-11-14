#coding: utf-8
import random;

def generation_solution():
    return (random.sample(range(0, 7), 5));


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

