'''Operações com bits'''

a = 5 # 0101
b = 3 # 0011

# AND
print(a & b) # 0001 = 1
# OR
print(a | b) # 0111 = 7
# XOR
print(a ^ b) # 0110 = 6
# NOT
print(~5) # -6

'''Shift (deslocamento)'''

# Para a esquerda (Multiplica por 2)
print(5 << 1) # 10
# Para a direta (Divide por 2)
print(5 >> 1) # 2

'''Manipulação de bytes'''

# Tipo bytes
b = bytes([65, 66, 67])
print(b)
# Tipo bytearray (Mutável)
a = bytes([77, 89, 254])
a[0] = 68
print(a)

'''Converter strings <-> bytes'''

# String -> bytes
texto = "Olá"
bTexto = texto.encode("utf-8")
print(bTexto)
# Bytes -> string 
tTexto = bTexto.decode("utf-8")
print(tTexto)

'''Converter inteiros <-> bytes'''
# Inteiro -> bytes
n = 384
nBytes = n.to_bytes(4, "big")
print(nBytes)
# Bytes -> Inteiro
bN = int.from_bytes(nBytes, "big")
print(bN)

'''Trabalhando com bits específicos'''

# & → verificar
# | → ligar
# ^ → alternar
# & ~ → desligar

# valor base << quantidade de deslocamentos

# 1 << 0 → 0001  (bit 0)
# 1 << 1 → 0010  (bit 1)
# 1 << 2 → 0100  (bit 2)
# 1 << 3 → 1000  (bit 3)

# Verificar o bit na posição 0
num = 5 # 0101
maskNum = (1 << 0) # 0001
print(num & maskNum) # 1
# Ativar bit
nume = 4 # 0100
maskNume = (1 << 1) # 0110
print(nume | maskNume) # 6 
# Desativar bit
numer = 6 # 0110 
maskNumer = ~(1 << 1) # 0100
print(numer & maskNumer) # 4 
# Alternar bit
numero = 5 # 0101
maskNumero = (1 << 0) # 0001
print(numero ^ maskNumero) # 4 (0100)

'''Uso de bits como permissões'''

# Cada bit representa algo
# bit 0 → leitura   (pode ver)
# bit 1 → escrita   (pode modificar)
# bit 2 → admin     (controle total)

# Em binário
# 0 → não tem permissão
# 1 → tem permissão

# Exemplo
# 000 → nenhuma permissão
# 001 → só leitura
# 010 → só escrita
# 011 → leitura + escrita
# 100 → só admin
# 111 → tudo