#coding: utf-8
from fct_master import *

print("\n\tDEBUT DU JEU\n...\n");
print("\tPOUR CONTINUER  TAPER 1\n...");
print("\tPOUR ABANDONNER TAPER 0\n...");
start = int(input("\tTAPER VOTRE CHOIX     "));

if not(start == 0 or start == 1 or (start > 48 and start < 57)):
    print("\n\tARrEt dE joUEr Au CoN !");
if (start == 0):
    print("VOUS ABANDONNEZ...REVENEZ PLUS TARD!!!");
if (start == 1):
    tentative = 1;
    while (tentative <= 10):
        combi = int(input("\n\tEntrer votre combinaison tentative {}\n...\t".format(tentative)));
        print("");
        tentative += 1;
    if (combi == 1 and True):
        print("\n...\tMon reuf t'as manger la verite ??\n\n...\tEn Sah t'es trop chaud wallah t'as gagner !!!!!");
        print("\n\tTa combi = {}, la mienne {}, t'es le nouveau BOSS!\n".format(combi, generation_solution()));
    if (tentative == 11):
        print("\tEchec, le Mastermind rester le BOSS\n");
        print("...\t", generation_solution());