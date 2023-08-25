'''3. Verifique se um inteiro positivo n é primo.'''

num= int(input('Número: '))

for i in range (2,num):
    if (num%i)==0:
        print(f'{num} é par')
        break
    else:
        print (f'{num} é impar')
        break