'''7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.'''

tamanho = int(input('Metros quadrados: '))
latas = round((tamanho/3)/18+0.5)
total = 80*latas

print(f'São necessárias {latas} latas no valor total de R$ {total:.2f} reais')
