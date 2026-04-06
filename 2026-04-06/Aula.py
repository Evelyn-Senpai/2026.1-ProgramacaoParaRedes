import struct
'''Endianness'''
# Forma como os bytes de um dado maior (como um número inteiro) são organizados na memória do computador.

# |     Tipo      |    Primeiro byte    | Mais usado onde |
# | ------------- | ------------------- | --------------- |
# | Big-endian    | Mais significativo	| Redes           |
# | Little-endian | Menos significativo | PCs modernos    |

# | Símbolo | Significado          |
# | ------- | -------------------- |
# | `<`     | Little-endian        |
# | `>`     | Big-endian           |
# | `!`     | Network (big-endian) |
# | `=`     | Padrão do sistema    |

# Força o empacotamento em 2 bytes usando a ordem Big-Endian
meuInt = 21579
meuIntBytes = meuInt.to_bytes(2, 'big') 
print(meuIntBytes) # Exibe o resultado binário/hexadecimal

# Desempacota garantindo a leitura correta
inteiro_original = int.from_bytes(meuIntBytes, 'big')

'''O Módulo struct'''
# Serve para converter dados entre tipos Python e representações binárias (bytes).

# Transforma valores em bytes
dados = struct.pack('i', 10)
print(dados)
# Faz o contrário
valor = struct.unpack('i', dados)
print(valor)

# | Código | Tipo            |
# | ------ | --------------- |
# | `i`    | inteiro         |
# | `f`    | float           |
# | `c`    | char            |
# | `s`    | string          |
# | `b`    | inteiro pequeno |

'''Endianness e Struct'''

# Little-endian
print(struct.pack('<I', 1))
# Big-endian
print(struct.pack('>I', 1))

# Empacotar
dados = struct.pack('>I', 305419896)  # 0x12345678
# Desempacotar
valor = struct.unpack('>I', dados)
print(dados)  # bytes
print(valor)  # (305419896,)