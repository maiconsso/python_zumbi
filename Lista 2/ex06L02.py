'''6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$'''
ganhohora = float(input('Ganho por hora: '))
horas = int(input('Horas trabalhada no mês: '))
total = ganhohora*horas
imposto = 11/100*total
inss = 8/100*total
sindicato = 5/100*total
totaliquido = total-(imposto+inss+sindicato)

print(f'Salário bruto R${total:.2f} reais e o  sálario líquido R${totaliquido:.2f} reais ')
print (f'Foi pago R${imposto+inss+sindicato:.2f} reais de desconto,sendo R${imposto:.2f} reais para IR , R${inss:.2f} reais para INSS \n e R${sindicato:.2f} reais para sindicato')