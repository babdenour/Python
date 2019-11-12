#coding: utf-8
#donner le nombre d'entier inferieur a la moyenne 
from Ftabrandom import tabrandom;
from Fmoyenne import moyenne;

def nbr_inf_moyene(tab):
    nifm = 0;
    while (tab < moyenne(tab)):
        nifm += 1;
    print(nifm);
    return (nifm);

nbr_inf_moyene();