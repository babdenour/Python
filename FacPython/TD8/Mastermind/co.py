#coding: utf-8

def compte_occurences(liste):
     
    liste = liste.split(" ");
    i = str(input("\n\tQuelle occurence vous cherchez ?\n...\t"));
    count = str(liste.count(i)).split(" ");
    
    print(count);
    print("\n\tliste + nbr d'occurence(s)\n\t", liste + count);
    print("taille de liste\n\t", len(liste) + 1);
    
liste = input("\n\tTa liste: ");
#compte_occurences(liste.split(" "));
compte_occurences(liste);