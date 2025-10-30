#Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci

n = int(input('Quantos valores deseja ver? '))

i = 0

prox = 1
ant = 1
atual = 1

while i < n:
    if i == 0:
        print('0')
    elif i == 1:
        print('1')
    elif i == 2:
        print('1')
    else:
        prox = ant + atual
        ant = atual
        atual = prox
        print(prox)
    i += 1