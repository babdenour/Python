#coding: utf-8


val1 = input("premiere  valeur entiere: ");
val2 = input("deuxieme  valeur entiere: ");
val3 = input("troisieme valeur entiere: ");
grand = int(val1);
moyen = int(val2);
petit = int(val3);

if((val1 < val2) and (val2 < val3)):
    grand = val3;
    petit = val1;
elif((val1 > val2) and (val1 < val3)):
    grand = val3;
    moyen = val1;
    petit = val2;
elif((val1 < val2) and (val2 > val3) and (val1 > val3)):
    grand = (val2);
    moyen = (val1);
    petit = (val3);
elif((val1 < val2) and (val2 > val3) and (val1 < val3)):
    grand = (val2);
    moyen = (val3);
    petit = (val1);
print("grand = {}, moyen = {}, petit = {}".format(grand, moyen, petit));