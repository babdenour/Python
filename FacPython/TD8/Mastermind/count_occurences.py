#coding: utf-8

def compte_occurences(liste):
    
    i = str(input("\n\tQuelle occurence vous cherchez ?\n...\t"));

    count = str(liste.count(i)).split(" ");
    print(count, "\n\n");
    print("liste + nbr d'occurence(s)\n\t", liste + count);

    print("taille de liste\n\t", len(liste) + 1);
    
liste = input("\n\tta liste: ").split(" ");
compte_occurences(liste);
