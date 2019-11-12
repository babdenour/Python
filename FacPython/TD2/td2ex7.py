#coding: utf-8

sec = input("Nombres de secondes (> 0) : ");
sec = int(sec);

if (sec > 0):
    secondes = sec % 60;
    minutes = sec % 3600 // 60;
    heure = sec // 3600;    
print("{} secondes correspond a {} heure(s), {} minute(s) et {} seconde(s)".format(sec,heure, minutes, secondes));
if (sec <= 0):
    print("Erreur,", sec, " < 0");