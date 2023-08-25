'''1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
nota = int(input("Insira uma nota 0 até 10: "))

while nota > 10:
    print ('Informe uma nota válida.')
    nota = int(input("Insira uma nota 0 até 10: "))
    

