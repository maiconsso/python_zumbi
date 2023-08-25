'''4. Faça um Programa que leia três números e mostre o maior deles.'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite segundo número: '))
num3 = int(input('Digite terceiro número: '))

if num1 >=num2 and num1 >=num3:
    print (f'{num1} é o maior número')
elif num2 >=num1 and num2 >=num3:
    print (f'{num2} é o maior número')
else:
     print (f'{num3} é o maior número')