'''
Fazer uma captura de pacotes no Wireshark e salvar em formato TCPDUM

Responder:
 - Quantos pacotes foram capturados
 - Quais os endereços MAC presentes
 - Quantos pacotes IPv4 existem
 - Considerando só IPv4 quantos pacotes TCP e UDP foram capturados
 - Quais as duas máquinas mais se "falaram"?(Considerar só IPv4) Quantos pacotes?
'''
import os

nomeArquivo = input('Digite o nome do arquivo: ') # Pega o arquivo no formato TCPDUMP.

diretorio = os.path.dirname(__file__) # Procura o arquivo na pasta que está esse exercício.
arquivo = os.path.join(diretorio, nomeArquivo) # Monta o caminho do arquivo.
abreArquivo = open(arquivo, "rb") # Abre o arquivo como bytes.

cabArquivo = abreArquivo.read(24) # Lê os primeiros 24 bytes do arquivo que é o HLEN (Cabeçalho)

magic = int.from_bytes(cabArquivo[:4], 'big') # Lê os 4 primeiros bytes do HLEN que é o Magic Number (Big ou Little Endian) para identificar a ordem dos bytes.
if magic in (0xA1B2C3D4, 0xA1B23C4D): # Verifica se os bytes do arquivo vão ser lidos como Big ou Little Endian
    endian = 'big'
else:
    endian = 'little'

cabPacote = abreArquivo.read(16) # Lê o cabeçalho do primeiro pacote (cada pacote tem 16 bytes).

MACs = set() # Coleção para armazenar MACs únicos.

quantPacotes = quantPACIPv4 = quantTCP = quantUDP = 0 # Contadores para: o número de pacotes, o número de pacotes IPv4, o número de segmentos TCPs nos pacotes IPv4, o número de segmentos UDPs nos pacotes IPv4. 

comunicacoes = {} # Dicionário para contar as comunicações entre IPs.

while cabPacote: # Enquanto no cabeçalho do pacote.

    quantPacotes += 1 # A cada cabeçalho de pacote aberto é mais um no contador de pacotes.

    tamanhoPac = int.from_bytes(cabPacote[8:12], endian) # Pega o tamanho capturado do pacote, o que vou realmente usar.

    pacote = abreArquivo.read(tamanhoPac) # Lê o tamanho do pacote capturado.

    if pacote[12:14] == b'\x08\x00': # Verifica se é IPv4, que é o que quero.
        
        quantPACIPv4 += 1 # Contador de pacotes IPv4 recebe mais um.

        protocolo = pacote[23] # Pega qual protocolo o pacote IPv4 está levando.

        if protocolo == 6: # Se for 6 é TCP.
            quantTCP += 1 # Contador de segmentos TCP recebe mais um.
        elif protocolo == 17: # Se for 17 é UDP
            quantUDP += 1 # Contador de segmentos UDP recebe mais um.

        ipOrigem = pacote[26:30] # Pega o IP de origem
        ipDestino = pacote[30:34] # Pega o IP de destino

        ipDipO = (ipOrigem, ipDestino) # Cria uma tupla com IP de destino e IP de origem.
        comunicacoes[ipDipO] = comunicacoes.get(ipDipO, 0) + 1 # Se a chave já existe, soma mais um, se não existe, começa com zero e soma mais um, ou seja, conta quantos pacotes existem entre esses dois IPs. 

    MACs.add(pacote[0:6]) # Adiciona o MAC de destino.
    MACs.add(pacote[6:12]) # Adiciona o MAC de origem.

    cabPacote = abreArquivo.read(16) # Lê o próximo pacote.

print('----------------------------------------------------------------')
print(f'Quantidade de pacotes: {quantPacotes}') # Print da quantidade de pacotes.
forMACs = set() # Coleção para armazenar MACs únicos formatados.
for MAC in MACs: # Pega cada MAC
    macFormatado = ':'.join(f"{x:02x}" for x in MAC) # Pega cada byte, converte em um hexadecimal de 2 dígitos, separa em :. 
    forMACs.add(macFormatado) # Adiciona o MAC formatado.
print(f'MACs: {forMACs}') # Print dos MACs formatados.
print(f'Quantidade de pacotes IPv4: {quantPACIPv4}') # Print da quantidade de pacotes IPv4.
print(f'Quantidade de segmentos TCP capturados: {quantTCP}') # Print da quantida de segmentos TCP capturados. 
print(f'Quantidade de segmentos UDP capturados: {quantUDP}') # Quantidade de segmentos UDP capturados.
if comunicacoes: # Se há comunicações registradas.
    maxComunicacoes = max(comunicacoes, key=comunicacoes.get) # Pega do par de IPs com o maior número de pacotes trocadosCC.
    qtd = comunicacoes[maxComunicacoes] # Pega o valor associado aos IPs de comunicaram.

    ip1 = '.'.join(map(str, maxComunicacoes[0])) # Converte o primeiro IP que está em Bytes para string dividos por '.'.
    ip2 = '.'.join(map(str, maxComunicacoes[1])) # Converte o segundo IP que está em Bytes para string dividos por '.'.

    print(f'Máquinas que mais se falaram: {ip1} -> {ip2} ({qtd} pacotes)') # Print das máquinas que mais se falaram e a quantidade de pacotes trocados.
print('----------------------------------------------------------------')
abreArquivo.close()    # Fechamento do arquivo.
