#coding: utf-8
#plusgrandevaleurabsolut

pe = input("Donnez un premier entier: ");
pe = int(pe);
se = input("Donnez un second entier: ");
se = int(se);
if (pe < 0):
    pe = -pe;
if (se < 0):
    se = -se;
if (pe == se):
    va = pe;
elif (pe > se):
    va = pe;
elif (pe < se):
    va = se;
print("La plus grane valeur absolue est {}".format(va));