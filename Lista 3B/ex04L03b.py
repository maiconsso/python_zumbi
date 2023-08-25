'''4. Dado um número inteiro positivo, determine a sua decomposição em fatores primos
calculando também a multiplicidade de cada fator.'''

num = int(input(' Numero : '))
x =0
fat =2
while num!=0:
    if num%fat ==0:
        num/=fat
        x +=1
    else:
        if x!=0:
            print(f'Fatores {fat} Multiplicidade {x}')
            x=0
        fat+=1
