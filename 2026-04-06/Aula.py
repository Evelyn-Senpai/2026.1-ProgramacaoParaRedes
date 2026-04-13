import struct
'''Endianness'''
# Forma como os bytes de um dado maior (como um número inteiro) são organizados na memória do computador.

# |     Tipo      |    Primeiro byte    | Mais usado onde |
# | ------------- | ------------------- | --------------- |
# | Big-endian    | Mais significativo	| Redes           |
# | Little-endian | Menos significativo | PCs modernos    |

# (Controle)
# | Símbolo | Significado                                      |
# | ------- | ------------------------------------------------ |
# | `<`     | Little-endian                                    |
# | `>`     | Big-endian                                       |
# | `!`     | Network (big-endian)                             |
# | `=`     | Nativo do sistema (sem alinhamento, padrão fixo) |
# | `@`     | Nativo do sistema (com alinhamento, nativo)      |

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
# | Código | Tipo                                   | Tamanho |      Significado      |
# | ------ | -------------------------------------- | ------- | --------------------- |
# | `b`    | inteiro com sinal (signed char)        | 1 byte  | Positivos e negativos |
# | `B`    | inteiro sem sinal (unsigned char)      | 1 byte  | Só positivos          |
# | `h`    | inteiro com sinal (short)              | 2 bytes | Positivos e negativos |
# | `H`    | inteiro sem sinal (unsigned short)     | 2 bytes | Só positivos          |
# | `i`    | inteiro com sinal (int)                | 4 bytes | Positivos e negativos |
# | `I`    | inteiro sem sinal (unsigned int)       | 4 bytes | Só positivos          |
# | `q`    | inteiro com sinal (long long)          | 8 bytes | Positivos e negativos |
# | `Q`    | inteiro sem sinal (unsigned long long) | 8 bytes | Só positivos          |

# Na rede
# | Campo           | Posição  |
# | --------------- | -------- |
# | Versão + IHL    | 1º valor |
# | Tipo de serviço | 2º valor |
# | Tamanho total   | 3º valor |
# | Identificação   | 4º valor |

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
