#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número. E no final, retorne também a quantidade de tentativas necessárias.

import random

pc = random.randint(1,10)
n = int(input('N: '))

tentativas = 1

while n != pc:
    n = int(input('N: '))
    tentativas += 1

print(f'Acertou com {tentativas} vezes')