#coding: utf-8

print("Veuillez entrer le nom d'un etudiant ainsi que ses trois notes");
nom = input("Entrer le nom de t'etudiant: ");
note1 = input("Entrer la note 1: ");
note2 = input("Entrer la note 2: ");
note3 = input("Entrer la note 3: ")

note1 = int(note1);
note2 = int(note2);
note3 = int(note3);
if (((note1 == 9) and (note2 == 9) and (note3 == 9)) or ((note1 + note2 + note3)//3 >= 10)):
    print("{} est admis".format(nom));
else:
    print("{} ets refuse".format(nom));