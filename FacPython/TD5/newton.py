#coding: utf-8

def factorielle(n):
    assert type(n) is int, "Factorielle d'un entier";
    fact = 1;
    for i in range(1, n + 1):
        fact = fact * i;
    return (fact);

def coefficient_binomial(n, k):
    assert type(n) is int, "n est un entier";
    assert type(k) is int, "k est un entier";
    coeff = factorielle(n) // (factorielle(k) * factorielle(n - k))
    return (coeff);

def newton(n):
    assert type(n) is int, "n est un entier";
    assert not (n == 0), "n different de 0";
    chaine = "(a + b)^" + str(n) + " = "
    for k in range(n + 1):
        c = coefficient_binomial(n, k);
        p = n - k;
        if not (c == 1):
            chaine = chaine + str(c);
        if not (p == 0):
            chaine = chaine + "a";
            if not  (p == 1):
                chaine = chaine + "^" + str(p);
        if not (k == 0):
            chaine = chaine + "b";
            if not (k == 1):
                chaine = chaine + "^" + str(k)
        if k < n:
            chaine = chaine + " + ";
    print(chaine);

n = int(input("Calculer le binome de newton pour n = "));
newton(n);