#Escreva um programa que crie um dicionário com as informações de 5 livros, como título, autor, ano de lançamento e número de páginas.
# Em seguida, exiba apenas os autores dos livros.

livros = {
    'O Hobbit': {'autor': 'J.R.R. Tolkien', 'ano': 1937, 'paginas': 310},
    'A Revolução dos Bichos': {'autor': 'George Orwell', 'ano': 1945, 'paginas': 152},
    '1984': {'autor': 'George Orwell', 'ano': 1949, 'paginas': 336},
    'O Pequeno Príncipe': {'autor': 'Antoine de Saint-Exupéry', 'ano': 1943, 'paginas': 96},
    'Dom Casmurro': {'autor': 'Machado de Assis', 'ano': 1899, 'paginas': 256}
}

for livro in livros.values():
    print(f'- {livro['autor']}')