'''6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
esperada para a viagem. '''

distancia = float(input('Qual a distancia em KM? '))
velocidade = float(input('Qual a velocidade média em Km/h? '))
tempo =  distancia/velocidade 
tempoconvertido = tempo*60

print (f'{int(tempoconvertido)} minutos')
