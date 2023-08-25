'''10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias.'''

cigarros = int(input('Quantos cigarros fumado por dia ? '))
anos = int(input('Quantos anos fumando? '))
cigarros_total = (anos*365)*cigarros
minutos_total = 10*cigarros_total
minutos_dias=(minutos_total/60)/24
print(f'Total de {round(minutos_dias+0.5)} dias perdidos.')