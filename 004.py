'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem o primeiro nome
'''

nome = input('Digite seu nome completo: ').strip()

#3.1
nome_sem_espaco = nome.replace(' ', '')

#3.2
quant_letras_nome = len(nome)
quant_letras_sem_espaco_v2 = quant_letras_nome - nome.count(' ')

#4.1
primeiro_nome = nome[0:nome.find(' ')]
quant_letras_1_nome = len(primeiro_nome)

print(f'Maiúsculas: {nome.upper()}'
      f'\nMinúsculas {nome.lower()}'
      f'\nQuantas letras sem espaço: {len(nome_sem_espaco)}'
      f'\nQuantas letras sem espaço: {quant_letras_sem_espaco_v2}'
      f'\nQuantidade de letras no 1 nome: {quant_letras_1_nome}')