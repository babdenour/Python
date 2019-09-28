#coding: utf-8
#exercice 6

name = input("Quel est ton prenom? ");
ln = input("Quel est ton nom ");

print("Bonjour{} {}!".format(name, ln));
date = input("En quelle annee es tu ne(e) ? ");
print("{} tu as, ou va avoir cette annee, {} ans".format(name, (2019 - int(date))));