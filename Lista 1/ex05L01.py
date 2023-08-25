'''5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
preço a pagar.'''

mercadoria = float(input('Qual o valor do produto? '))
desconto = float(input('Quantos porcentos de desconto? '))
desconto_mercadoria = mercadoria*desconto/100
resultado = mercadoria-desconto_mercadoria

print (f' O desconto é de R${desconto_mercadoria:.2f} reais e valor da mercadoria fica R${resultado:.2f} reais.')