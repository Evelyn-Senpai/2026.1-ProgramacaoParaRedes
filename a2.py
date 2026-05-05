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
- Se o protocolo transportado no IPv4 for ICMP:
  - Mostre o nome do tipo do pacote (basta cinco, ignore outros)
  - Para ```echo request``` e ```echo reply```, mostre o número de identificação e o número de sequência.
- Se o protocolo transportado no IPv4 for UDP:
  - Mostre as portas de origem e destino do datagrama;
- Se o protocolo transportado no IPv4 for TCP:
  - Mostre as portas de origem e destino do datagrama;
  - Exiba mais quatro campos a sua escolha;
    
Ao final, mostre:
- o IP da máquina que mais trocou dados usando IPv4 com a máquina de captura, indicando a quantidade de bytes.
- qual o intervalo de tempo em que os pacotes foram capturados.

Não é permitido o uso de bibliotecas não nativas do Python.
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

MACs = set() # Coleção para armazenar MACs únicos.
IPs = set() # Coleção para armazenar os IPv4.

while cabPacote:

  tamanhoPac = int.from_bytes(cabPacote[8:12], endian) # Pega o tamanho capturado do pacote, o que vou realmente usar.

  pacote = abreArquivo.read(tamanhoPac) # Lê o tamanho do pacote capturado.

  MACs.add(pacote[0:6]) # Adiciona o MAC de destino.
  MACs.add(pacote[6:12]) # Adiciona o MAC de origem.

  if pacote[12:14] == b'\x08\x00': # Verifica se é IPv4, que é o que quero.

    protocolo = pacote[23] # Pega qual protocolo o pacote IPv4 está levando.

    versao = pacote[14] >> 4 # Pega o primeiro byte do IPv4 (a versão do protocolo IPv4 (4)).

    IPs.add(pacote[26:30]) # Adiciona o IP de origem
    IPs.add(pacote[30:34]) # Adiciona o IP de destino

  cabPacote = abreArquivo.read(16) # Lê o próximo pacote.

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

forMACs = set() # Coleção para armazenar MACs únicos formatados.
for MAC in MACs: # Pega cada MAC
  macFormatado = ':'.join(f"{x:02x}" for x in MAC) # Pega cada byte, converte em um hexadecimal de 2 dígitos, separa em :. 
  forMACs.add(macFormatado) # Adiciona o MAC formatado.
print('----------------------------------------------------------------')
print(f'MAC addresses de destino e origem do frame: {forMACs}') # Print dos MACs formatados.
print('----------------------------------------------------------------')
forIPs = set() #Coleção para armazenar IPv4 únicos formtados.
for IP in IPs:
  ipFormatado = '.'.join(map(str, IP))
  forIPs.add(ipFormatado) # Adiciona o IP formatado.
print(f'Endereços IPv4 de destino e origem: {forIPs}') # Print dos IPs formatados.
print(f'Protocolo que o IPv4 está levando: {protocolo}') # Print de qual protocolo o pacote IPv4 está levando.
print(f'Versão do IPv4: {versao}')
print('----------------------------------------------------------------')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
abreArquivo.close()    # Fechamento do arquivo.