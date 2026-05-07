'''
## A rota do fotógrafo (30 pontos)

<hr/>

Desenvolva um programa que receba na linha de comando um diretório.
Identifique na pasta as fotos em formato **JPEG** com informações de **EXIF** e, particularmente, a geolocalização (latitude e longitude). 

Entre as fotos escolha até 10 e mostre uma rota entre elas, apresentando-a no **google maps**.  Um exemplo de URL para criar/mostrar uma rota é: ```https://www.google.com/maps/dir/-5.79448,-35.2110/-5.80000,-35.2600/-5.82000,-35.3000```. 

As únicas bibliotecas permitidas são ```subprocess``` e ```struct```. 
'''
import sys, os

pasta = sys.argv[1] # A pasta que será digitada na linha de comando.

fotos = os.listdir(pasta) # Uma lista das fotos que estão na pasta.

for foto in fotos: # Pega cada nome de cada uma das fotos.
    caminho = os.path.join(pasta, foto) # Pega o caminho que a foto está, ou seja, pega a foto.

    abreFoto = open(foto, 'rb') # Abre em formatado de bytes.

    idJPEG = abreFoto[:4] # Pega os quatro primeiros bytes da foto.
    print(idJPEG)

    abreFoto.close() # Fechamento da foto.