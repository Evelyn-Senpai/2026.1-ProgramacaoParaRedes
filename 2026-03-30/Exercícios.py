'''1'''
a = 6 # 0110
b = 2 # 0010
print(a & b) # 2
print(a | b) # 6
print(a ^ b) # 4
'''2'''
print(7 << 1) # 14
print(8 >> 2) # 2
'''3'''
print(10 & 4) # 1010 & 0100 = 0000 -> 0
'''4'''
mask = 1 << 3 # 1000
print(mask) # 8
'''5'''
num = 10 # 1010
mask = 1 << 0 # 0001
print(num & mask) # 0
'''6'''
num = 8 # 1000
mask = 1 << 0 # 0001
print(num | mask) # 10
'''7'''
num = 7 # 0111
mask = ~(1 << 1) # 1101
print(num & mask) # 5
'''8'''
num = 5 # 0101
mask = 1 << 2 # 0100
print(num ^ mask) # 1
'''9'''
num = 0 # 0000
mask = (1 << 0) | (1 << 2) | (1 << 3)
print(num | mask) # 13
'''10'''
num = 13 # 1101
mask = 1 << 3 # 0111
print(num ^ mask) # 5
'''11'''
def verificar_bit(num, bit):
    if num & (1 << bit):
        return True
    else:
        return False
# Programa principal
print(verificar_bit(5, 0)) # True
print(verificar_bit(5, 1)) # False
'''12'''
def ligar_bit(num, pos):
    return (num | (1 << pos))
# Programa principal
print(ligar_bit(8, 0)) # 9
'''13'''
def desligar_bit(num, pos):
    return (num & ~(1 << pos))
# Programa principal 
print(desligar_bit(7, 1)) # 5
'''14'''
def alternar_bit(num, pos):
    return (num ^ (1 << pos))
# Programa principal
print(alternar_bit(5, 2)) # 1
'''15'''
def sistema_permissoes(p):
    ativaLeituraEscrita = ((p | (1 << 0)) | (p | (1 << 1))) # 0011
    if (ativaLeituraEscrita & (1 << 2)) != 0:
        return ativaLeituraEscrita # 0111
    else:
        ativaAdmin = (ativaLeituraEscrita | (1 << 2))
        return ativaAdmin # 0111
# Programa principal
permissao = 0 # 0000
print(sistema_permissoes(permissao)) # 7
'''16'''
def impar_par(n): # Com if
    if (n & (1 << 0) != 0):
        print('Ímpar')
    else:
        print('Par')
def impar_par(n): # Sem if
    print(['Par', 'Ímpar'][n & 1])
# Programa principal 
num = 7
impar_par(num) # Ímpar
'''17'''
def conta_bit(n):
    cont = 0
    strN = str(n)
    for i in strN:
        if (n & (1 << n[i])):
            cont += 1
    return cont
# Programa principal
num = 13 # 1101
print(conta_bit(num)) # 3