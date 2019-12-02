#coding: utf-8
from fct_master import *

i = 0;
combi = [];
rbp = "pion(s) bien place(s)"; 
rmp = "pion(s) mal place";

print("\n\tDEBUT DU JEU\n...\n");
print("\tPOUR CONTINUER  TAPER 1\n...");
print("\tPOUR ABANDONNER TAPER 0\n...");
start = int(input("\tTAPER VOTRE CHOIX     "));

if not(start == 0 or start == 1):
    print("\n\tARrEt dE joUEr Au CoN !");
if (start == 0):
    print("VOUS ABANDONNEZ...REVENEZ PLUS TARD!!!");
if (start == 1):
    tentative = 1;
    sol = generation_solution();
    while (tentative < 11):
        print("\n\tEntrer votre combinaison tentative {}\n...\t".format(tentative));
        while (len(combi) < 5):
            print("\n\tProposez la couleur", i + 1);
            k = int(input("\t"));
            if (k >= 0 and k < 8):
                combi.append(k);
             #   print("\n\tbien couleur placer", nb_bien_places_couleur(combi, sol, couleur));
                i += 1;
        i = 0;
        print("{} {} et {} {}".format(nb_bien_places(combi, sol), rbp, nb_couleurs_mal_placees(combi, sol), rmp));
        print(sol);
        print(combi);
        tentative += 1;   
        if (combi == sol):
            print("\n...\tMon reuf t'as manger la verite ??\n\n...\tEn Sah t'es trop chaud wallah t'as gagner !!!!!");
            print("\n\tTa combinaison = {}\n\tLa mienne {}, \n\tT'es le nouveau BOSS!\n\n\tPsahteck wallah Psahteck!!!".format(combi, sol));
            break;
        combi = [];
        print("\n\tEchec, le Mastermind rester le BOSS\n");
        print("\n\tVOULEZ VOUS CONTINUER ?\n...\n");
        print("\tPOUR CONTINUER  TAPER 1\n...");
        print("\tPOUR ABANDONNER TAPER 0\n...");
        encore = int(input("\tTAPER VOTRE CHOIX     "));
        if (encore == 0):
            print("VOUS ABANDONNEZ...REVENEZ PLUS TARD!!!");
            break;
    if (tentative > 10):
        print("\n\tEchec, le Mastermind rester le BOSS\n");
        print("...\t", sol);