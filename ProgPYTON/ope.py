#coding:utf-8

op1 = input("premier op: ");
operant = input("operant: ");
op2 = input("second op: ");

op1 = int(op1);
op2 = int(op2);

#transtipage type int
if ((operant == '*') or (operant == '/') or (operant == '%') or (operant == '-') or (operant == '+')):
    if operant == '*':
        resultat = float(op1 * op2);
    if (operant == '/') and (op2 != 0):
        resultat = float(op1 / op2);
    if operant == '%':
        resultat = int(op1 % op2);
    if operant == '-':
        resultat = float(op1 - op2);
    if operant == '+':
        resultat = float(op1 + op2);
if ((op2 == 0) and (operant == '/')):
    print("error division by 0 impossible");
if (op1 >= '1' ):
print("{} {} {}".format(op1, operant, op2));
print("{}".format(resultat));