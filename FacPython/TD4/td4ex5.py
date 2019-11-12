#coding: utf-8

print("\tEntrer la taille de votre list: ");
taille = int(input('\t'));
i = 0;
min = 0;
max = 0;
somme = 0;
lst = [ ];

for i in range(taille):
    print("\tEntrer l'entier situer a l'indice ", i + 1);
    nbr = int(input('\t'));
    lst.append(nbr);
    somme = somme + nbr;
    if (nbr < min):
        min = nbr;
    if (nbr > max):
        max = nbr;    
print("\n\t", lst);
print("\n\tmin {}, max {}, somme {}".format(min, max, somme));