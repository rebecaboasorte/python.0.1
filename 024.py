#Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso

numeros_extenso = (
    "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete",
    "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze"
)

try:
    n = int(input('Digite um número entre 0 e 15: '))
    while n < 0 or n > 15:
        n = int(input('Digite um número entre 0 e 15: '))
    print(f'Seu número por extenso é = {numeros_extenso[n]}')
except ValueError:
    print('Digite apenas números ')