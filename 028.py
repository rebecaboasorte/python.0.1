'''
Faça um programa que leia o nome e o QI de várias pessoas, guardando tudo e uma lista. No final mostre:

1. Quantas pessoas foram cadastradas
2. Uma listagem com as pessoas com o maior QI
3. Uma listagem com as pessoas de menor QI
'''

Pessoas = [[], []]

while True:
    nome = input('Nome[sair para terminar]: ')
    if nome == 'sair':
        break

    Pessoas[0].append(nome)
    Pessoas[1].append(int(input('QI: ')))

print(f'A quantidade de registros é {len(Pessoas[0])}')

maiores_qis = sorted(Pessoas[1], reverse=True)
menores_qis = sorted(Pessoas[1])

print(f'Os QIs em ordem decrescente {sorted(Pessoas[1], reverse=True)}')
for i in maiores_qis:
    print(Pessoas[0][Pessoas[1].index(i)])

print(f'Os QIs em ordem crescente {sorted(Pessoas[1])}')
for i in menores_qis:
    print(Pessoas[0][Pessoas[1].index(i)])



