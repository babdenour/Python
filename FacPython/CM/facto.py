#coding: utf-8

n = input("entre un premier nbr ");
n = int(n);
i = 2;
fact = 1;

while (i <= n):
    fact = fact * i;
    i += 1;
print("fact de {} est {}".format(n, fact));