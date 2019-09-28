#coding: utf-8

#exercice 4

p = 5;
q = 3 * p;

print("p vaut", p, "et q vaut", q, "leur somme fait", p + q);
print("q est-il un multiple de p ?", q%p == 0);

tmp = p;
p = q;
q = tmp;