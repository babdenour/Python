#coding: utf-8

a = input("Entrer le nombre a multiplier : ");
a = int(a);
i = 1;

while (i <= a):
    print("Table de multiplication de", i, ":");
    j = 1;
    while (j <= 10):
        print("{} * {} = {}".format(i, j, i * j));
        j += 1;
    i += 1;