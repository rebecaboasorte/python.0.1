#Escreva um programa que leia diversos alunos,
# crie um dicionário com as notas de dele em três disciplinas:
# matemática, português e história. Em seguida, exiba a média das notas dos alunos.

alunos = {}

while True:
    nome = input('Nome[fim para parar]: ')
    if nome == 'fim':
        break
    matematica = float(input('Matemática: '))
    portugues = float(input('Portugês: '))
    historia = float(input('História: '))

    alunos[nome] = {'Matemática': matematica, 'Português': portugues, 'História': historia}

for nome, notas in alunos.items():
    media = sum(notas.values()) / len(notas)
    print(f'A média do Aluno {nome} é {round(media, 2)}')

