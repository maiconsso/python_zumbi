'''2. Determine se um ano é bissexto. Verifique no Google como fazer isso..
Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)'''

ano = int(input('Digite o ano: '))
if (ano % 4 == 0 and ano%100!= 0) or (ano%400==0):
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')