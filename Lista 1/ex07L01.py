'''7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32'''

temperatura= float(input('Qual a temperatura? '))
conversao = (9*temperatura)/5+32
print (f'{conversao:.1f}°F')