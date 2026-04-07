import struct
'''Endianness'''
# Forma como os bytes de um dado maior (como um número inteiro) são organizados na memória do computador.

# |     Tipo      |    Primeiro byte    | Mais usado onde |
# | ------------- | ------------------- | --------------- |
# | Big-endian    | Mais significativo	| Redes           |
# | Little-endian | Menos significativo | PCs modernos    |

# (Controle)
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

# (Formatos)
# | Código | Tipo                                   | Tamanho |
# | ------ | -------------------------------------- | ------- |
# | `b`    | inteiro com sinal (signed char)        | 1 byte  |
# | `B`    | inteiro sem sinal (unsigned char)      | 1 byte  |
# | `h`    | inteiro com sinal (short)              | 2 bytes |
# | `H`    | inteiro sem sinal (unsigned short)     | 2 bytes |
# | `i`    | inteiro com sinal (int)                | 4 bytes |
# | `I`    | inteiro sem sinal (unsigned int)       | 4 bytes |
# | `q`    | inteiro com sinal (long long)          | 8 bytes |
# | `Q`    | inteiro sem sinal (unsigned long long) | 8 bytes |

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
