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
import os, sys

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

nPacotes = 0 # Para contar o número de pacotes.

comunicacoes = {} # Dicionário para as máquinas que mais trocaram dados usando IPv4.

tempInicial = None # Para pegar o tempo que começou a captura.
tempFinal = None # Para pegar o tempo final da captura.

while cabPacote: # Percorre cada pacote.
  tempS = int.from_bytes(cabPacote[0:4], endian) # Pega o tempo em segundos.
  tempM = int.from_bytes(cabPacote[4:8], endian) # Pega o tempo em microssegundos.

  tempo = tempS + (tempM / 1_000_000) # O tempo vai ser o tempo em segundos + o tempo em microssegundos em fração de segundos. 

  if tempInicial is None: # Para atualizar os tempos.
    tempInicial = tempo

  tempFinal = tempo

  nPacotes += 1 # A cada pacote recebe mais um.

  print(f'--- PACOTE {nPacotes} ---') # Para visualizar o número do pacote

  tamanhoPac = int.from_bytes(cabPacote[8:12], endian) # Pega o tamanho capturado do pacote, o que vou realmente usar.

  pacote = abreArquivo.read(tamanhoPac) # Lê o tamanho do pacote capturado.

  macDestino = ':'.join(f"{x:02x}" for x in pacote[0:6]) # Pega o MAC de destino, em cada byte converte em um hexadecimal de 2 dígitos e separa por :.
  macOrigem = ':'.join(f"{x:02x}" for x in pacote[6:12]) # Pega o MAC de origem, em cada byte converte em um hexadecimal de 2 dígitos e separa por :.
  print(f'MAC addresses de destino: {macDestino}') # Print do MAC de destino.
  print(f'MAC addresses de origem: {macOrigem}') # Print do MAC de origem.

  if pacote[12:14] == b'\x08\x00': # Verifica se é IPv4.
    inicioIPv4 = 14 # Define o inicio do IPv4, que é fixo.

    ipDestino = pacote[inicioIPv4+12:inicioIPv4+16] # Pega o IP de destino do IPv4.
    ipOrigem = pacote[inicioIPv4+16:inicioIPv4+20] # Pega o IP de origem do IPv4.
    print(f'IP de destino: {'.'.join(map(str, pacote[inicioIPv4+16:inicioIPv4+20]))}') # Print do IP de destino que está dentro do IPv4 em bytes e converte cada parte em string dividindo por '.'.
    print(f'IP de origem: {'.'.join(map(str, pacote[inicioIPv4+12:inicioIPv4+16]))}') # Print do IP de origem que está dentro do IPv4 em bytes e converte cada parte em string dividindo por '.'.

    ipDipO = tuple(sorted([ipOrigem, ipDestino])) # Cria uma tupla com IP de destino e IP de origem, independente da ordem.
    comunicacoes[ipDipO] = comunicacoes.get(ipDipO, 0) + tamanhoPac # Se a chave já existe, soma mais o tamanho do pacote, se não existe, começa com zero e soma mais o tamanho do pacote, ou seja, conta quantos bytes foram trocados entre esses dois IPv4s.

    protocolo = pacote[inicioIPv4+9] # Pega qual protocolo o pacote IPv4 está levando.
    print(f'Protocolo: {protocolo}') # Print de qual protocolo o pacote IPv4 está levando. 

    versao = pacote[inicioIPv4] >> 4 # Pega os quatros primeiros bits do IPv4 (a versão do protocolo IPv4 (4)).
    print(f'Versão do pacote IPv4: {versao}') # Print da versão do IPv4 (4).

    tosIPv4 = pacote[inicioIPv4+1] # Pega o tipo de serviço que o pacote IPv4 está levando.
    print(f'Tipo de serviço IPv4: {tosIPv4}') # Print do tipo do serviço IPv4.

    tamIPv4 = int.from_bytes(pacote[inicioIPv4+2:inicioIPv4+4], 'big') # Pega o tamanho do pacote IPv4 ('big' porque pacotes IPv4 sempre são big endian).
    print(f'Tamanho do pacote IPv4: {tamIPv4} bytes') # Print do tamanho do pacote IPv4.

    ihl = pacote[inicioIPv4] & 0x0F # Pega os últimos quatro bits do IPv4 (ihl que define o tamanho do cabeçalho do IPv4).
    tamCabIPv4 = ihl * 4 # O ihl * 4 bytes (tamanho da palavra do IHL) é o tamanho do cabeçalho IPv4.

    if protocolo == 1: # Se o protocolo for ICMP.
      inicioICMP = inicioIPv4 + tamCabIPv4 # o início do ICMP vai ser início do pacote IPv4 + o tamanho do cabeçalho IPv4.
      
      tipo = pacote[inicioICMP] # Pega o primeiro byte do ICMP que é o tipo.
      tiposICMP = { # Dicionário com os cincos primeiros nomes dos tipos de ICMP.
        0: 'Echo Reply',
        8: 'Echo Request',
        3: 'Destination Unreachable',
        11: 'Time Exceeded',
        5: 'Redirect'
      }

      nome = tiposICMP.get(tipo, None) # Busca o nome do tipo ICMP no dicionário.
      if nome: # Se o tipo tiver um nome.
        print(f'ICMP: {nome}') # Print do nome do tipo de ICMP.

        if tipo in (0, 8): # Se o tipo de ICMP for 0 (Echo Reply) ou 8 (Echo Request).
          identificador = int.from_bytes(pacote[inicioICMP+4:inicioICMP+6], 'big') # Transforma o identificador do tipo de ICMP em um número inteiro.
          print(f'Identificador: {identificador}') # Print do identificador do tipo do ICMP. 

          sequencia = int.from_bytes(pacote[inicioICMP+6:inicioICMP+8], 'big') # Transforma o número de sequência do tipo de ICMP em um número inteiro.
          print(f'Número de sequência: {sequencia}') # Print do número de sequência do tipo do ICMP. 

    elif protocolo == 17: # Se o protocolo for UDP. 
      inicioUDP = inicioIPv4 + tamCabIPv4 # O início do UDP vai ser o início do pacote IPv4 + o tamanho do cabeçalho IPv4.

      pDestino = int.from_bytes(pacote[inicioUDP+2:inicioUDP+4], 'big') # Transforma a porta de destino do UDP em um número inteiro.
      print(f'UDP porta destino: {pDestino}') # Print da porta UDP de destino.

      pOrigem = int.from_bytes(pacote[inicioUDP:inicioUDP+2], 'big') # Transforma a porta de origem do UDP em um número inteiro.
      print(f'UDP porta origem: {pOrigem}') # Print da porta UDP de origem.

    elif protocolo == 6:
      inicioTCP = inicioIPv4 + tamCabIPv4 # O início do TCP vai ser o início do pacote IPv4 + o tamanho do cabeçalho IPv4.

      if len(pacote) >= inicioTCP + 18: # Para evitar pacotes TCP incompletos?
        pDestino = int.from_bytes(pacote[inicioTCP+2:inicioTCP+4], 'big') # Transforma a porta de destino do TCP em um número inteiro. 
        print(f'TCP porta destino: {pDestino}') # Print da porta TCP de destino.

        pOrigem = int.from_bytes(pacote[inicioTCP:inicioTCP+2], 'big') # Transforma a porta de origem do TCP em um número inteiro.
        print(f'TCP porta origem: {pOrigem}') # Print da porta TCP de origem.

        ack = int.from_bytes(pacote[inicioTCP+8:inicioTCP+12], 'big') # Transforma o número de confirmação do TCP em um número inteiro.
        print(f'TCP número de confirmação: {ack}') # Print do número de confirmação do TCP.

        seq = int.from_bytes(pacote[inicioTCP+4:inicioTCP+8], 'big') # Transforma o número de sequência do TCP em um número inteiro.
        print(f'TCP número de sequência: {seq}') # Print do número de sequência do TCP.

        win = int.from_bytes(pacote[inicioTCP+14:inicioTCP+16], 'big') # Transforma a janela (controle de fluxo) do TCP em um número inteiro.
        print(f'TCP janela: {win}') # Print da janela do TCP.

        che = int.from_bytes(pacote[inicioTCP+16:inicioTCP+18], 'big') # Transforma o checksum (detecção de erros) do TCP em um número inteiro.
        print(f'TCP checksum: {che}') # Print do checksum do TCP.

  print('-------------------------------')

  cabPacote = abreArquivo.read(16) # Lê o próximo pacote.

if comunicacoes: # Se há comunicações registradas.
  maxComunicacoes = max(comunicacoes, key=comunicacoes.get) # Pega do par de IPv4s com o maior número de bytes trocados.
  qtd = comunicacoes[maxComunicacoes] # Pega o valor associado aos IPv4s que mais trocaram dados.

  ip1 = '.'.join(map(str, maxComunicacoes[0])) # Converte o primeiro IP que está em Bytes para string dividos por '.'.
  ip2 = '.'.join(map(str, maxComunicacoes[1])) # Converte o segundo IP que está em Bytes para string dividos por '.'.

  print(f'IP das máquinas que mais se falaram: {ip1} -> {ip2} ({qtd} bytes)') # Print do IP das máquinas que mais se falaram e a quantidade de bytes trocados.

if tempInicial is not None and tempFinal is not None: # Ao final, pega o tempo inicial e final.
  intervalo = tempFinal - tempInicial # Cálculo do intervalo.
  
  print(f'Intervalo da captura: {intervalo:.6f} segundos') # Print do intervalo de tempo das capturas em segundos.

abreArquivo.close()    # Fechamento do arquivo.