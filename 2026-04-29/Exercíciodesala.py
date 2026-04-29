'''
Fazer uma captura de pacotes no Wireshark e salvar em formato TCPDUM

Responder:
 - Quantos pacotes foram capturados
 - Quais os endereços MAC presentes
 - Quantos pacotes IPv4 existem
 - Considerando só IPv4  quantos pacotes TCP e UDP foram captirados
 - Quais as duas máquinas mais se "falaram"?(Considerar só IPv4) Quantos pacotes?
'''
from datetime import datetime 
import os

nomeArquivo = input('Digite o nome do arquivo: ')

diretorio = os.path.dirname(__file__)
arquivo = f'{diretorio}\\{nomeArquivo}'
abreArquivo = open(arquivo, "rb")

cabArquivo = abreArquivo.read(24)

magic = int.from_bytes(cabArquivo[:4], 'big')
if magic in (0xA1B2C3D4, 0xA1B23C4D):
    endian = 'big'
else:
    endian = 'little'

cabPacote = abreArquivo.read(16)
while cabPacote != b'':
    quantPAcotes += 1
    tempoS = int.from_bytes(cabPacote[:4], endian)
    tempoTXT = datetime(tempoS)
    
    
    tempoMS = cabPacote[4:8]

    tamanhoPac = int.from_bytes(cabPacote[8:12], endian)
    tamanhoOrig = cabPacote[12:16]
    
    abreArquivo.seek(tamanhoPac, 1)

    cabPacote = abreArquivo.read(16)

abreArquivo.close()    
print(f'Quantidade de pacotes: {quantPAcotes}')