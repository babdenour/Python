#coding: utf-8
#division euclidienne

dividende = input("entier positif ou nul     (dividende) : ");
dividende = int(dividende);
diviseur =  input("entier strictement positif (diviseur) : ");
diviseur = int(diviseur);

if ((diviseur != 0 and dividende >= 0)):
    quotient = dividende // diviseur;
    reste = dividende % diviseur;
    print("Voici la division euclidienne de {} par {} :".format(dividende, diviseur));
    print("{} = {} * {} + {}".format(dividende, diviseur, quotient, reste));
else:
    print("Erreur, diviseur negatif ou nul");