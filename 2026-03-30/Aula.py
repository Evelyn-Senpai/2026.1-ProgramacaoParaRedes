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

'''Converter string <-> bytes'''

# String -> bytes
texto = "Olá"
bTexto = texto.encode("utf-8")
print(bTexto)
# Byres -> string 
tTexto = bTexto.decode("utf-8")
print(tTexto)

'''Trabalhando com bits específicos'''

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