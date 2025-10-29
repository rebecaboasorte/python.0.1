#Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário

try:
    #Entrada de dados
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    cidade_de_nascimento = input('Digite a cidade de nascimento: ')

    #Saída de dados
    print(f'Seu nome é {nome} com {idade} anos e nasceu em {cidade_de_nascimento}')
except:
    print('Não aceitamos letras')