'''
## A rota do fotógrafo (30 pontos)

<hr/>

Desenvolva um programa que receba na linha de comando um diretório.
Identifique na pasta as fotos em formato **JPEG** com informações de **EXIF** e, particularmente, a geolocalização (latitude e longitude). 

Entre as fotos escolha até 10 e mostre uma rota entre elas, apresentando-a no **google maps**.  Um exemplo de URL para criar/mostrar uma rota é: ```https://www.google.com/maps/dir/-5.79448,-35.2110/-5.80000,-35.2600/-5.82000,-35.3000```. 

As únicas bibliotecas permitidas são ```subprocess``` e ```struct```. 
'''
import sys

nomeJPEG = sys.argv[1] # Pega o nome da foto JPEG que foi digitado na linha de comando.

abreJPEG = open(nomeJPEG, 'rb') # Abre a foto JPEG e lê como bytes.

cabJEP = abreJPEG.read(4) # Pega os quatro primeiros bytes da foto JPEG.

identificador = int.from_bytes(cabJEP, 'big') & 0x0F

if identificador == b'\xff\xe1':
    print('É EXIF')


abreJPEG.close()