'''1. Dizemos que um número natural é triangular se ele é produto de três números naturais
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n,
verificar se n é triangular.
'''
num = int(input("Número: "))
k = 1

while k * (k+1) * (k+2) < num:
    k+=1

if k * (k+1) * (k+2) == num:
    print(f'{num} é Triangular')
else:
    print(f'{num} não é Triangular')
