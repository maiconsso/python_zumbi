'''2. Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
nenhuma delas esteja em falta no caixa.
'''

valor = float(input('Entre com o valor: '))
notas = [50, 20, 10, 5, 2, 1]
i = 0

while valor > 0 :
    div = valor/notas[i]
    valor =valor%notas[i]
    if div != 0:
        print(f'{int(div)} notas de R${notas[i]:.2f} reais')
    i+=1
