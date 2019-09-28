#coding:utf-8

age = input("choisir age : ");
nbr_personne = input("combien y a t-il de personnes ? ");
txt = "il y a {} personnes qui ont {} ans\n";
t_bool = True;
f_bool = False;

print("il y a", nbr_personne, "personnes qui ont", age, "ans\n");
print(txt.format(nbr_personne, age));
print("il y a {} personnes qui ont {} ans\n".format(nbr_personne, age));

print(type(age));
print(type(nbr_personne));
print(type(txt));

age = int(age);
print(type(age));

print(type(t_bool));
print(t_bool);
t_bool = int(t_bool);
print(t_bool);
print(type(f_bool));
print(f_bool);
f_bool = int(f_bool);
print(f_bool);