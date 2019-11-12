#coding: utf-8
#cinema

nbr = input("nombre(s) de ticket(s): ");
nbr = int(nbr);

if (nbr <= 0):
    print("nombres de place nul");
if (nbr <= 5):
    prix = nbr * 8;
elif (nbr > 5 and nbr < 10):
    prix = 5 * 8 + (nbr - 5) * 6;
elif (nbr > 10):
    prix = 5 * 8 + 5 * 6 + (nbr - 10) * 5.50
print("Le prix total pour {} tickets est de {} euros".format(nbr, prix));