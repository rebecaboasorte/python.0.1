#Crie um programa para jogar JOKEMPO, usando a função random.randint

import random
import time

pc = random.randint(1, 3)
j = int(input('1. Pedra'
              '\n2. Papel'
              '\n3. Tesoura ---> '))
time.sleep(1)
print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO')
time.sleep(1)
print('Ainda pensando')
time.sleep(1)
print('...')
time.sleep(1)

if pc == j:
    print('Empate')
elif (pc == 1 and j == 2) or (pc == 2 and j == 3) or (pc == 3 and j == 1):
    print(f'Ganhou pc -{pc} x {j} - j')
else:
    print(f'Perdeu pc -{pc} x {j} - j')

