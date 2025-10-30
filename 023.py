'''
Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

Apenas os 3 primeiros mais assistidos
Os últimos 2 mais assistidos
A lista em ordem alfabética
Em que posição está “O rei leão”
'''


filmes = (
    "O Poderoso Chefão",
    "O Senhor dos Anéis: O Retorno do Rei",
    "Titanic",
    "A Lista de Schindler",
    "Pulp Fiction: Tempo de Violência",
    "O Rei Leão",
    "Forrest Gump: O Contador de Histórias",
    "Matrix",
    "Os Infiltrados",
    "O Silêncio dos Inocentes"
)

print(f'Os 3 mais assistidos são {filmes[:3]}'
      f'\nOs últimos 2 mais assistidos {filmes[-2:]}'
      f'\nA lista em ordem alfabética {sorted(filmes)}'
      f'\nO Rei Leão está na posição {filmes.index('O Rei Leão') + 1}')

