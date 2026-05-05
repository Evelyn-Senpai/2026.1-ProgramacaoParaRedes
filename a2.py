'''
## Análise de pacotes de rede (20 pontos)

<hr/>

A avaliação de pacotes que trafegam numa rede pode ser útil em muitos casos. A captura do tráfego acontece por meio de programas como *tcpdump*, *pcap* e *winpcap* (ou mesmo em interfaces mais amigáveis, como o *Wireshark*), gerando o que se conhece por formato <b>pcap</b>.
 
O formato do arquivo pcap está disponível em: ```https://datatracker.ietf.org/doc/id/draft-gharris-opsawg-pcap-00.html```

Faça um programa que recebe o nome de um arquivo <b>pcap</b> na linha de comando e **exiba para cada pacote capturado**:

- Os *MAC addresses* de origem e destino do frame;
- Se o protocolo transportado no enlace for IPv4:
  - Mostre os endereços IPv4 de origem e destino;
  - Outros quatro campos do IPv4 à sua escolha;
'''
import os

nomeArquivo = input('Digite o nome do arquivo: ') # Pega o arquivo no formatado TCPDUMP.

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

while cabPacote: # Percorre cada pacote.
  print('--- PACOTE ---')

  tamanhoPac = int.from_bytes(cabPacote[8:12], endian) # Pega o tamanho capturado do pacote, o que vou realmente usar.

  pacote = abreArquivo.read(tamanhoPac) # Lê o tamanho do pacote capturado.

  macDestino = ':'.join(f"{x:02x}" for x in pacote[0:6]) # Pega o MAC de destino, em cada byte converte em um hexadecimal de 2 dígitos e separa por :.
  macOrigem = ':'.join(f"{x:02x}" for x in pacote[6:12]) # Pega o MAC de origem, em cada byte converte em um hexadecimal de 2 dígitos e separa por :.
  print(f'MAC addresses de destino: {macDestino}') # Print do MAC de destino.
  print(f'MAC addresses de origem: {macOrigem}') # Print do MAC de origem.

  if pacote[12:14] == b'\x08\x00': # Verifica se é IPv4.
    ipDestino = '.'.join(map(str, pacote[30:34])) # Pega o IP de destino em bytes e converte cada parte em string dividindo por '.'.
    ipOrigem = '.'.join(map(str, pacote[26:30])) # Pega o IP de origem em bytes e converte cada parte em string dividindo por '.'.
    print(f'IP de destino: {ipDestino}') # Print do IP de destino.
    print(f'IP de origem: {ipOrigem}') # Print do IP de origem.

    protocolo = pacote[23] # Pega qual protocolo o pacote IPv4 está levando.
    print(f'Protocolo: {protocolo}') # Print de qual protocolo o pacote IPv4 está levando. 

    versao = pacote[14] >> 4 # Pega o primeiro byte do IPv4 (a versão do protocolo IPv4 (4)).
    print(f'Versão do pacote IPv4: {versao}') # Print da versão do IPv4 (4).

    tosIPv4 = pacote[15] # Pega o tipo de serviço que o pacote IPv4 está levando.
    print(f'Tipo de serviço IPv4: {tosIPv4}') # Print do tipo do serviço IPv4.

    tamIPv4 = int.from_bytes(pacote[16:18], 'big') # Pega o tamanho do pacote IPv4 ('big' porque pacotes IPv4 sempre são big endian).
    print(f'Tamanho do pacote IPv4: {tamIPv4} bytes') # Print do tamanho do pacote IPv4.
  
  cabPacote = abreArquivo.read(16) # Lê o próximo pacote.

abreArquivo.close()    # Fechamento do arquivo.