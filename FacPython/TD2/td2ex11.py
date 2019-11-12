#coding: utf-8
#ordinaux anglais

n = input("Entrer un entier: ");
n = int(n);

if (n == 1 or n % 10 == 1 and n != 11):
    print("",n,"st");
elif (n == 2 or n % 10 == 2 and n != 12):
    print("",n,"nd");
elif (n == 3 or n % 10 == 3 and n != 13):
    print("",n,"rd");
else :
    print("",n,"th");