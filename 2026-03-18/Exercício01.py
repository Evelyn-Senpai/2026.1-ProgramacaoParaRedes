'''
Seja d(n) definido como a soma dos divisores próprios d n(números menores que n que dividem)
n exatamente).
Se d(a) = b e d(b) = a, onde a != b, então a e b formam um par de números amigáveis, e cada
um deles é chamado de número amigável.
Por exemplo, os divisores próprios de 220 são 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 e 110;
portanto, d(220) = 284. Os divisores próprios de 284 são 1, 2 4, 71 e 142; então d(284) = 220.
Calcule a soma de todos os números amigáveis menores que 10000.
'''

print('SEM FUNÇÕES')
soma_total = 0
for a in range(1, 10001):
    soma_div_a = 0
    for i in range(1, a):
        if a % i == 0:
            soma_div_a += i
    b = soma_div_a
    soma_div_b = 0
    for i in range(1, b):
        if b % i == 0:
            soma_div_b += i
    if a != b and a == soma_div_b and a < b:
        print(f"{a} é amigo de {b}")
        soma_total += a + b
print(f'A soma de todos os números amigáveis é: {soma_total:.0f}')

print('COM FUNÇÕES')
def f_a(A):
    soma_div_a = 0
    for i in range(1, A):
        if A % i == 0:
            soma_div_a += i
    return soma_div_a

def f_b(B):
    soma_div_b = 0
    for i in range(1, B):
        if B % i == 0:
            soma_div_b += i
    return soma_div_b

soma_total = 0
for a in range(1, 10000):
    b = f_a(a)
    r = f_b(b)
    if a != b and a == r and a < b:
        print(f'{a} é amigo de {b}')
        soma_total += a + b
print(f'A soma de todos os números amigáveis é: {soma_total:.0f}')

print('COM UMA ÚNICA FUNÇÃO')
def soma_a_b(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma

soma_total = 0
for a in range(1, 10000):
    b = soma_a_b(a)
    r = soma_a_b(b)
    if a != b and a == r and a < b:
        print(f'{a} é amigo de {b}')
        soma_total += a + b
print(f'A soma de todos os números amigáveis é: {soma_total:.0f}')