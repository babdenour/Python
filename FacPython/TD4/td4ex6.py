#coding: utf-8

taille = int(input("\tCombien d'entier comporte votre liste ? "));
i = 0;
n = 0;
list = [ ];

for i in range(taille):   
    print("\n\tQuel est l'entier ", i + 1," de votre list");
    nbr = int(input('\t'));
    list.append(nbr);
    print("Votre liste est la suivante: {}".format(list));

for o in range(0, taille - 1):
    if (list[o] > list[o + 1]):
        n = 1;
if (i == 1):
    print("Elle est pas triee")
else:
    print("Elle n'est pas triee"); 