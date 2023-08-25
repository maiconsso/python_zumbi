'''1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.'''

num1 = int(input('Lado 1 do triângulo: '))
num2 = int(input('Lado 2 do triângulo: '))
num3 = int(input('Lado 3 do triângulo: '))

if num1 + num2 < num3 or num1 + num3 < num2 or num2 + num3 < num1:
    print('Não é um triângulo')
elif num1 == num2 == num3:
    print('Triângulo Equilátero')
elif num1 == num2 or num2 == num3 or num1 == num3:
    print('Triângulo isósceles')
else:
    print('Triângulo escalo')
    