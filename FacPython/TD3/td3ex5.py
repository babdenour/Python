#coding: utf-8
#calcule moyenne note

note_saisie = 0;
note_min = 20;
note_max = 0;
indice_min = 0;
indice_max = 0;
i = 0;
m = 0.0;

while (note_saisie <= 20 and note_saisie >= 0):
    print("veuillez entrer la note numero", i + 1);
    note_saisie = float(input());
    i += 1;
    if (note_saisie <= 20 and note_saisie >= 0):
        m =  m + note_saisie;
    if (note_min > note_saisie and note_saisie >= 0):
        note_min = note_saisie;
        indice_min = i;
    if (note_max < note_saisie and note_saisie <= 20):
        note_max = note_saisie;
        indice_max = i;
if (i > 1):
    m = m / (i - 1);
    print("nbr notes: {}, note min: {}, indide min: {}, note max: {}, indice max: {}, moyen: {}"
.format(i, note_min, indice_min, note_max, indice_max, m));
else:
    print("erreur");
    