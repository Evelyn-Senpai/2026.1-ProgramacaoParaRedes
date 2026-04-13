import struct
ipv4 = str(input('Digite o número IPv4: ')) # 192.168.1.10
num = int(input('Digite a máscara: ')) # 24
octeto = ipv4.split('.')
ip = (int(octeto[0]) << 24) | (int(octeto[1]) << 16) | (int(octeto[2])) << 8 | (int(octeto[3]))
mask = (0xFFFFFFFF << (32 - num)) & 0xFFFFFFFF
rede = struct.unpack('!BBBB', (ip & mask).to_bytes(4, 'big'))
print('A rede é: ', end= '')
for i in rede:
    print(i, end= ' ')