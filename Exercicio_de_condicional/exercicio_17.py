c = float(input('Digite a temperatura em Celsius para converter para Fahrenheit: '))

f = (9 * c + 160) / 5

print(f"A temperatura farenheit eh: {f}")

if f < 65:
    print('Ele ira vestir: bermudas')
else:
    print('Ele ira vestir: calça')

