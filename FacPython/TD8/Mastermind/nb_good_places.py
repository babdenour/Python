#coding: utf-8

def nb_bien_places(proposition, solution):
    i = 0;
    npbp = 0;
    while (i < len(proposition)):
        if (proposition[i] == solution[i]):
            npbp += 1;
        i += 1;
    return (npbp);