"""def recherche_sequentielle_liste_triee(liste, elem):
    if (elem > liste[len(liste) - 1]):
     return (False);
    else :
        i = 0;
        while (liste[i] < elem):
            i += 1;
        if (liste [i] == elem):
            return (True);
        else :
            return (False);
1: 
2: meilleur cas calcules de comlexcite = min(cout(d) * d e Dn) = 1
3: pire cas calcules de comlexcite = max(cout(d) * d, d e Dn) = n * 3
4: complexciter moyenne = E cout(d) * p(d)
"""
def myster(liste, elem):
    for i in range(len(liste)):
        if (liste[i] == elem):
            resultat[0] = resultat[0] + 1;
            resultat[2] = i;
            if (resultat[1] == -1):
                resultat[1] = i;
    return (resultat);

"""
"""