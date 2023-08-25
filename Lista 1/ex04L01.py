'''4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
porcentagem do aumento. Exiba o valor do aumento e do novo salário.'''

salario=float(input('Qual seu salário? '))
aumento=float(input('Quantos porcentos? '))
aumento_salario = salario*aumento/100
totalsalario = aumento_salario+salario
print (f'Você teve um aumento de R${aumento_salario:.2f} reais e seu novo salário é R${totalsalario:.2f} reais')