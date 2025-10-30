#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

n = int(input('Digite um número: '))

for i in range(11):
    print(f'{n} X {i} = {n * i}')