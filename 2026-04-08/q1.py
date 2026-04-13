import struct
ipv4 = str(input('Digite o número IPv4: ')) # 192.168.1.10
mask = int(input('Digite a máscara (entre 2 e 32): ')) # 24 -> 255.255.255.0
print(struct.pack('>i', mask))
rede = mask >> 4
print()