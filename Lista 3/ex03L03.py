'''3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento
'''
pais1= 80000
pais2= 200000
anos = 0
while pais1 < pais2:
    pais2 *= 1.015
    pais1 *= 1.03
    anos += 1
print (anos)
