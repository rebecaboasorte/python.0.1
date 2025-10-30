'''
Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

V = (4/3) . π . r³
A = 4 . π . r²
'''

raio = float(input('Digite o raio da esfera: '))

V = (4/3) * 3.1415 * raio ** 3
A = 4 * 3.1415 * raio ** 2

print(f'Volume da Esfera: {V:.2f}\nÁrea da esfera: {round(A, 2)}')


