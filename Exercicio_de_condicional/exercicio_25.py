# 25. O Peso normal de uma criança pode ser calculado através da fórmula:
# PesoNormal = idade - 6 / 4.4 + 2.3 * (idade - 6) + 2
#  Escreva um programa que leia a idade e o peso de uma criança e, se for o caso, imprima
# uma dessas mensagens de acordo com a quantidade de quilos acima do peso com que a
# criança esteja:
# Quantidade de quilos acima do peso
# De 2 a 5
# Acima de 5 ate 10
# Acima de 10
# Mensagem
# “Parar de tomar refrigerante.”
# “Parar de comer doces.”
# “Parar de tomar refrigerante e de comer doces.”

idade = int(input('Digite sua idade: '))

PesoNormal = Idade - 6 / 4.4 + 2.3 * (idade - 6) + 22

if 2 <= idade <= 5:
    print("Para de tomar refrigerante")
elif 5 <= idade <= 10:
    print("Para de comer doces")

print("")