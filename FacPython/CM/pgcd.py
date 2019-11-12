#coding: utf-8

a = input("a = ");
b = input("b = ");
a = int(a);
b = int(b);

if (a < b):
    tmp = a;
    a = b;
    b = tmp;

a_init = a;
b_init = b;

while (b != 0):
    n = a // b;
    r = a % b;
    a = b;
    b = r;
print("Le pgcd de {} et {} est {}".format(a_init, b_init, a));