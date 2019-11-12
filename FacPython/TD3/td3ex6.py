#coding: utf-8
#pyramide

hauteur = int(input("Entrez un entier: "));

for i in range(1, hauteur + 1):
    print(" " * (hauteur - i), "*" * ((2 * i) - 1));