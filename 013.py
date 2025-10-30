#Faça um programa que leia um número e retorne o fatorial !

n = int(input('N: '))

i = 1
fat = 1

while i < (n + 1):
    fat *= i
    i += 1

print(f'O fatorial de {n} é {fat}')