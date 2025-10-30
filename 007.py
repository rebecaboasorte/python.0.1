'''
Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
'''

letra = input('Digite uma letra: ').strip().lower()[0]

if letra in 'aeiou':
    print('É vogal')
else:
    print('Consoante')
