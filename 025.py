#Escreva um programa que crie uma lista com varios números lidos pelo usuário,
# em seguida, exiba apenas os números ímpares da lista.

def retorna_impar(y):
    return [x for x in y if x % 2 != 0]

numeros = []
while True:
    try:
        n = input('número[0000 para sair]: ')
        if n == '0000':
            break
        numeros.append(int(n))
    except ValueError:
        print('Digite apenas números')

print(f'Lista ímpares = {retorna_impar(numeros)}')

for i in numeros:
    if i % 2 != 0:
        print(i)
