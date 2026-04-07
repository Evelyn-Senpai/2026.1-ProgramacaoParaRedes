'''1'''
print('O primeiro byte é o mais significativo.')
print('O primeiro byte é o menos significativo.')
'''2'''
print('Endereço 0: 12, endereço 1: 34, endereço 2: 56, endereço 3: 78.')
print('Endereço 0: 78, endereço 1: 56, endereço 2: 34, endereço 3: 12.')
'''3'''
print('Porque é assim que dados com mais de um byte são transmitidos na arquitetura TCP/IP,e para garantir que todos os dispositivos interpretem os dados da mesma forma.')
'''4'''
print('A função struck.pack() transforma valores em bytes e a função struck.unpack() faz o contrário.')
'''5'''
print('Para o tipo inteiro pequeno.')
print('Para o tipo inteiro de dois bytes.')
print('Para o tipo inteiro.')
print('Para o tipo float.')
'''6'''
print('Little-endian.')
print('Big-endian.')
print('Network (Big-endian)')
'''7'''
import struct
num = 1000
converteLittleEndian = struct.pack('<i', num)
converteBigEndian = struct.pack('>i', num)
print(converteLittleEndian) # b'\x03\xe8\x00\x00'
print(converteBigEndian) # b'\x00\x00\xe8\x03'
'''8'''
import struct
dados = struct.pack('>h', 500)
print(dados) # b'\x01\xf4'
'''9'''
import struct
dados = b'\x00\x64'
desempacoteBigEndian = struct.unpack('>h', dados)
desempacoteLittleEndian = struct.unpack('<h', dados)
print(desempacoteBigEndian) # 100
print(desempacoteLittleEndian) # 25600