'''
Crie um programa que pede ao usuário para digitar dois números e, em seguida, divide o primeiro número pelo segundo número.
No entanto, o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido, como uma string ou o número zero.

ZeroDivisionError ; ValueError

'''

try:
    n1 = int(input('Digite um n: '))
    n2 = int(input('Digite um n: '))

    print(f'a divisão é {n1 / n2}')

except ZeroDivisionError:
    print('Não dividimos por 0')
except ValueError:
    print('Aceitamos apenas números')
