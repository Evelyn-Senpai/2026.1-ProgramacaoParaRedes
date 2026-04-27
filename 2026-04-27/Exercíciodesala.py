from datetime import datetime

nomeArquivo = input('Digite o nome do arquivo: ')

fd = open(nomeArquivo, "rb")

cabArquivo = fd.read(24)
magic = int.from_bytes(cabArquivo[:4], 'big')
if magic in (0xA1B2C3D4, 0xA1B23C4D):
    endian = 'big'
else:
    endian = 'little'

if magic == 0xA1B2C3D4:
    tempoAdicional = "us"
else:
    tempoAdicional = 'ns'

cabPacote = fd.read(16)

while cabPacote != b'':
    tempoS = int.from_bytes(cabPacote[:4], endian)
    tempoTXT = datetime.utcfromtimestamp(tempoS)
    
    tempoEX = int.from_bytes(cabPacote[4:8], endian)
    input(f'{tempoTXT}.{tempoEX} {tempoAdicional}')

    tempoMS = cabPacote[4:8]

    tamanhoPac = int.from_bytes(cabPacote[8:12], endian)
    tamanhoOrig = cabPacote[12:16]
    
    fd.seek(tamanhoPac, 1)
    
    cabPacote = fd.read(16)

fd.close()