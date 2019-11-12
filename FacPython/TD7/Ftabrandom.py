import random


def tabrandom():
    srmx = int(input("shufle random max  = "))
    tmax = int(input("taille de tab = "))
    if (srmx <= tmax):
        print("le nombre d'elements a randomiser doit etre superieur au nombre de place ds le tab ");
        return (-1);    
    else :
        max = 1;
        imax = 1;
        i = 0;
        tab = random.sample(range(1, srmx), tmax);
        print(tab);
        while (i < len(tab)):
            if (tab[i] > max):
                max = tab[i];
                imax = i;
            i += 1;
        print("\nNombre max = {}, Position = {}.".format(max, imax));
    return (tab);