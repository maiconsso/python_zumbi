'''5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides. '''

num = int(input("Número: "))
num2 = int(input("Segundo Número: "))

while num%num2 != 0:
    num,num2 = num2, num%num2
    
print (f'MDC = {num2}')