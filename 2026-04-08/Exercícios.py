# '''1'''
# print('O primeiro byte é o mais significativo.')
# print('O primeiro byte é o menos significativo.')
# '''2'''
# print('Endereço 0: 12, endereço 1: 34, endereço 2: 56, endereço 3: 78.')
# print('Endereço 0: 78, endereço 1: 56, endereço 2: 34, endereço 3: 12.')
# '''3'''
# print('Porque é assim que dados com mais de um byte são transmitidos na arquitetura TCP/IP,e para garantir que todos os dispositivos interpretem os dados da mesma forma.')
# '''4'''
# print('A função struck.pack() transforma valores em bytes e a função struck.unpack() faz o contrário.')
# '''5'''
# print('Para o tipo inteiro pequeno.')
# print('Para o tipo inteiro de dois bytes.')
# print('Para o tipo inteiro.')
# print('Para o tipo float.')
# '''6'''
# print('Little-endian.')
# print('Big-endian.')
# print('Network (Big-endian)')
# '''7'''
# import struct
# num = 1000
# converteLittleEndian = struct.pack('<i', num)
# converteBigEndian = struct.pack('>i', num)
# print(converteLittleEndian) # b'\x03\xe8\x00\x00'
# print(converteBigEndian) # b'\x00\x00\xe8\x03'
# '''8'''
# import struct
# dados = struct.pack('>h', 500)
# print(dados) # b'\x01\xf4'
# '''9'''
# import struct
# dados = b'\x00\x64'
# desempacoteBigEndian = struct.unpack('>h', dados)
# desempacoteLittleEndian = struct.unpack('<h', dados)
# print(desempacoteBigEndian) # 100
# print(desempacoteLittleEndian) # 25600
# '''10'''
# import struct
# pacote = b'\x45\x00\x00\x28'
# print(struct.unpack('!BBH', pacote)) # 69 0 40
# print('Tamanho total = ', 40)
# print('Versão = ', 69 >> 4)
# '''11'''
# print('! -> Garante que seja Big-endian.')
# print('B -> Primeiro valor de tamanho 1 byte sendo os 4 primeiros bits a versão e os 4 últimos bits o IHL.')
# print('B -> Segundo valor de tamanho 1 byte sendo o tipo de serviço.')
# print('H -> Terceiro valor de tamanho 2 bytes sendo o tamanho total.')
# print('H -> Quarto valor de tamanho 2 bytes sendo a identificação.')
# '''12'''
# print('Para garantir que os dados estejam no padrão de rede(Big-endian).')
# '''13'''
# import struct
# pacote = b'\x45\x00\x00\x3c\x1c\x46'
# print(struct.unpack('!BBHH', pacote)) # 69 0 60 7238
# print('Versão = ', 69 >> 4) # 4
# print('IHL = ', 69 & 0x0f) # 5
# print('Tamanho total = ', 60) # 60
# print('Versão + IHL → indica a versão do protocolo e o tamanho do cabeçalho\n' \
#     'Tipo de serviço → define prioridade/qualidade do pacote\n' \
#     'Tamanho total → tamanho total do pacote\n' \
#     'Identificação → identifica o pacote (fragmentação)')
# '''14'''
# print('A informação será interpretada incorretamente, porque o pacote vai ser interpretado com a ordem de bytes invertida, podendo causar erros como tamanhos inválidos, identificação incorreta e falhas na comunicação.')
# '''15'''
# import struct
# pacote = b'\x01\x00'
# desempacoteBigEndian = struct.unpack('>h', pacote) # 256
# desempacoteLittleEndian = struct.unpack('<h', pacote) # 1
# print(desempacoteBigEndian)
# print(desempacoteLittleEndian)
# print('Os valores são diferentes porque os bytes são interpretados em ordens diferentes. No Big-endian, o primeiro byte o mais significativo, enquanto no Little-endian o primeiro byte o menos significativo, resultando valores diferentes.')
# '''16'''
# print('Os dados em um computador são armazenados na memória como uma sequência de bytes. A endianness define a ordem em que esses bytes são organizados na memória, podendo ser big-endian ou little-endian. Durante a transmissão de dados, como em redes, é necessário que os dispositivos utilizem uma ordem padrão de bytes para garantir que a informação seja interpretada corretamente. Por isso, protocolos como o IPv4 utilizam big-endian. Caso a endianness não seja respeitada, os dados podem ser interpretados incorretamente.')
# '''17'''
# import struct
# def empacote_bigendian(n):
#     return struct.pack('>i', n)
# def desempacote_bigendian(x):
#     return struct.unpack('>i', x)[0]
# num = int(input('Informe um número inteiro: ')) # 28
# pacote = empacote_bigendian(num) 
# print(pacote) # b'\x00\x00\x00\x1c'
# print(desempacote_bigendian(pacote)) # 28
# '''18'''
# print('O módulo struct é essencial ao trabalhar com protocolos como o IPv4 e o Ethernet porque permite converter dados binários em valores interpretáveis, de acordo com a estrutura definida pelos protocolos. Ele facilita a leitura e escrita de campos específicos, respeitando o tamanho e a ordem dos bytes (endianness), evitando erros na interpretação dos dados.')
'''19'''
import struct
def desempacote(p):
    return struct.unpack('!BBHH', p)
def versao(d):
    return d[0] >> 4
def ihl(d):
    return d[0] & 0x0F
def tamanho_total(d):
    return d[2]
def identificacao(d):
    return d[3]
pacote = b'\x45\x00\x00\x54\xa6\xf2' 
dados = desempacote(pacote) # 69 0 84 42738
print(versao(dados)) # 4
print(ihl(dados)) # 5
print(tamanho_total(dados)) # 84
print(identificacao(dados)) # 42738