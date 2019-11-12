from Ftabrandom import tabrandom;

def moyenne(tab):
    somme = 0;
    i = 0;
    m = 0;
    while (i < len(tab)):
        somme = somme + tab[i];
        i += 1;
    m = somme / len(tab)    
    return (m);