'''9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.'''

kilometros = float(input('Kilometros percorridos: '))
dias = int(input('Dias alugado: '))
diaria = 60*dias
kmrodado = (15/100)*kilometros
total_pagar = diaria+kmrodado

print(f'Total a pagar R${total_pagar:.2f} reais')