'''Faça um programa que peça um número e faça seu fatoriaç'''

def fatorial(numero):
    f = 1
    for i in range(numero, 0, -1):
        f *= i
    return f
num = int(input('Informe um número: '))
print('Seu fatorial é: ', end='')
print(fatorial(num))
