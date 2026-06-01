import struct
ipv4 = str(input('Digite o número IPv4: '))
num = int(input('Digite a máscara: '))
octeto = ipv4.split('.') # Separa o endereço ipv4 em 4 partes
ip = (int(octeto[0]) << 24) | (int(octeto[1]) << 16) | (int(octeto[2]) << 8) | (int(octeto[3])) # Convertendo cada parte em um número inteiro, e juntando em um único número de 32 bits
mask = (0xFFFFFFFF << (32 - num)) & 0xFFFFFFFF # 32 é o tamanho do ipv4, então é subtraido num deste valor para achar quantos bits sobram para o host, 0xFFFFFFFF é 32 bits iguais a 1, então os bits de hosts são deslocados para esquerda ficando com 0 (porque não quero os hosts), e no final é feito um and com 0xFFFFFFFF para garantir que o resultado fique com 32 bits, a máscara é criada em formato inteiro, resultado = 255.255.255.0
rede = struct.unpack('!BBBB', (ip & mask).to_bytes(4, 'big')) # Primeiro: transforma o resultado do ip and mask (a rede) em bytes, Segundo: Desempacota esse número, tornando ele em uma tupla onde os resultados são seus respectivos valores em decimal.
gateway = struct.unpack('!BBBB', ((ip & mask) + 1).to_bytes(4, 'big')) # O gateway é o primeiro endereço da rede, então primeiro é somado mais 1 no endereço de rede, só então esse resultado é transformado em bytes e desempacotado.
broadcast = struct.unpack('!BBBB', ((ip & mask) | (~mask & 0xFFFFFFFF)).to_bytes(4, 'big')) # O broadcast é o maior endereço da rede, então é pego a rede e feito um or com a inversão dos bits da máscara limitada a 32 bits.
hosts = ((2 ** (32 - num)) - 2) # Achados os bits de hosts, então 2^8 é quantidade de endereços, mas sempre vai existir dois endereços já definidos, rede e broadcast, então subtraimos 2.
print('--------------------------------------------------------')
print('A rede é: ', end= '')
for i in rede: # Print da rede 
    print(i, end= ' ')
print('\nO broadcast é: ', end= '')
for i in broadcast: # Print do broadcast
    print(i, end=' ')
print('\nO gateway é: ', end= '')
for i in gateway: # Print do gateway
    print(i, end=' ')
print('\nA quantidade de hosts é: ', hosts) # Print dos hosts
print('--------------------------------------------------------')