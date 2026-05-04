'''
Fazer uma captura de pacotes no Wireshark e salvar em formato TCPDUM

Responder:
 - Quantos pacotes foram capturados
 - Quais os endereços MAC presentes
 - Quantos pacotes IPv4 existem
 - Considerando só IPv4 quantos pacotes TCP e UDP foram capturados
 - Quais as duas máquinas mais se "falaram"?(Considerar só IPv4) Quantos pacotes?
'''
from datetime import datetime 
import os

nomeArquivo = input('Digite o nome do arquivo: ')

diretorio = os.path.dirname(__file__)
arquivo = os.path.join(diretorio, nomeArquivo)
abreArquivo = open(arquivo, "rb")

cabArquivo = abreArquivo.read(24)

magic = int.from_bytes(cabArquivo[:4], 'big')
if magic in (0xA1B2C3D4, 0xA1B23C4D):
    endian = 'big'
else:
    endian = 'little'

cabPacote = abreArquivo.read(16)
MACs = set()
quantPacotes = 0
pacIPv4 = 0
tcp = udp = 0
conexoes = {}
while cabPacote:
    quantPacotes += 1

    tamanhoOrig = cabPacote[12:16]
    tamanhoPac = int.from_bytes(cabPacote[8:12], endian)

    pacote = abreArquivo.read(tamanhoPac)

    if pacote[12:14] == b'\x08\x00':
        pacIPv4 += 1

        protocolo = pacote[23]

        if protocolo == 6:
            tcp += 1
        elif protocolo == 17:
            udp += 1

        ipOrigem = pacote[26:30]
        ipDestino = pacote[30:34]

        chave = (ipOrigem, ipDestino)
        conexoes[chave] = conexoes.get(chave, 0) + 1

    tempoS = int.from_bytes(cabPacote[:4], endian)
    tempoTXT = datetime.fromtimestamp(tempoS)
    
    
    tempoMS = cabPacote[4:8]
    
    MACs.add(pacote[0:6])
    MACs.add(pacote[6:12])

    cabPacote = abreArquivo.read(16)

print('----------------------------------------------------------------')
print(f'Quantidade de pacotes: {quantPacotes}')
forMACs = {':'.join(f"{x:02x}" for x in MAC) for MAC in MACs}
print(f'MACs: {forMACs}')
print(f'Quantidade de pacotes IPv4: {pacIPv4}')
print(f'Quantidade de pacotes TCP capturados: {tcp}')
print(f'Quantidade de pacotes UDP capturados: {udp}')
if conexoes:
    maxConexoes = max(conexoes, key=conexoes.get)
    qtd = conexoes[maxConexoes]

    ip1 = '.'.join(map(str, maxConexoes[0]))
    ip2 = '.'.join(map(str, maxConexoes[1]))

    print(f'Máquinas que mais se falaram: {ip1} -> {ip2} ({qtd} pacotes)')
print('----------------------------------------------------------------')
abreArquivo.close()    
