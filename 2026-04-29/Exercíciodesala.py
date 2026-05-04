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

nomeArquivo = input('Digite o nome do arquivo: ') # Pega o arquivo no formatado TCPDUMP.

diretorio = os.path.dirname(__file__) # Procura o arquivo na pasta que está esse exercício.
arquivo = os.path.join(diretorio, nomeArquivo) # Monta o caminho do arquivo.
abreArquivo = open(arquivo, "rb") # Abre o arquivo como bytes.

cabArquivo = abreArquivo.read(24) # Lê os primeiros 24 bytes do arquivo que é o HLEN (Cabeçalho)

magic = int.from_bytes(cabArquivo[:4], 'big') # Lê os 4 primeiros bytes do HLEN que é o Magic Number (Big ou Little Endian).
endian = ''
if magic == 0xA1B2C3D4: # Verifica se os bytes do arquivo vão ser lidos como Big ou Little Endian
    endian = 'big'
elif magic == 0xA1B23C4D:
    endian = 'little'

cabPacote = abreArquivo.read(16) # Lê o cabeçalho do primeiro pacote (cada pacote tem 16 bytes).

MACs = set() # Coleção para armazenar MACs únicos.

quantPacotes = quantPACIPv4 = quantTCP = quantUDP = 0 # Contadores para: o número de pacotes, o número de pacotes IPv4, o número de protocolos TCPs nos pacotes IPv4, o número de protocolos UDPs nos pacotes IPv4. 

conexoes = {} # Dicionário para contar as comunicações entre IPs.

while cabPacote: # Enquanto no cabeçalho do pacote.

    quantPacotes += 1 # A cada cabeçalho de pacote aberto é mais um no contador de pacotes.

    tamanhoOrig = cabPacote[12:16] # Pega o tamanho original do pacote.

    tamanhoPac = int.from_bytes(cabPacote[8:12], endian) # Pega o tamanho capturado do pacote, o que vou realmente usar.

    pacote = abreArquivo.read(tamanhoPac) # Lê o tamanho do pacote capturado.

    if pacote[12:14] == b'\x08\x00': # Verifica se é IPv4, que é o que quero.
        
        quantPACIPv4 += 1 # Contador de pacotes IPv4 recebe mais um.

        protocolo = pacote[23] # Pega qual protocolo o pacote IPv4 está levando.

        if protocolo == 6: # Se for 6 é TCP.
            quantTCP += 1 # Contador de protocolos TCP recebe mais um.
        elif protocolo == 17: # Se for 17 é UDP
            quantUDP += 1 # Contador de protocolos UDP recebe mais um.

        ipOrigem = pacote[26:30] # Pega o IP de origem
        ipDestino = pacote[30:34] # Pega o IP de destino

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
print(f'Quantidade de pacotes IPv4: {quantPACIPv4}')
print(f'Quantidade de pacotes TCP capturados: {quantTCP}')
print(f'Quantidade de pacotes UDP capturados: {quantUDP}')
if conexoes:
    maxConexoes = max(conexoes, key=conexoes.get)
    qtd = conexoes[maxConexoes]

    ip1 = '.'.join(map(str, maxConexoes[0]))
    ip2 = '.'.join(map(str, maxConexoes[1]))

    print(f'Máquinas que mais se falaram: {ip1} -> {ip2} ({qtd} pacotes)')
print('----------------------------------------------------------------')
abreArquivo.close()    
