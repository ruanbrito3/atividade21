# Exercício Python 21: Faça um programa que mostre na tela uma contagem regressiva para o estouro de
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
contagem = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for item in contagem:
    print(item)
    sleep(1)
else:
    print("pouuuu")