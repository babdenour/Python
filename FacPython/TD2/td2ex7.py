#coding:utf-8
#pasfini

sec = input("Nombres de secondes (> 0) : ");
sec = int(sec);

if (sec > 0):
    if (sec > 60):
        secondes = sec % 60;
    if (minutes ):
        minutes = sec / 60;
    if (heure ):
        heure = sec // 3600;    
    print("{} secondes correspond a {} heure(s), {} minute(s) et {} seconde(s)".format(sec,heure, minutes, secondes));
if (sec < 0):
    print("Erreur,", sec, " < 0");