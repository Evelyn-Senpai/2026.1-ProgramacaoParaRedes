'''
## A rota do fotógrafo (30 pontos)

<hr/>

Desenvolva um programa que receba na linha de comando um diretório.
Identifique na pasta as fotos em formato **JPEG** com informações de **EXIF** e, particularmente, a geolocalização (latitude e longitude). 

Entre as fotos escolha até 10 e mostre uma rota entre elas, apresentando-a no **google maps**.  Um exemplo de URL para criar/mostrar uma rota é: ```https://www.google.com/maps/dir/-5.79448,-35.2110/-5.80000,-35.2600/-5.82000,-35.3000```. 

As únicas bibliotecas permitidas são ```subprocess``` e ```struct```. 
'''
import sys
# print('----------')
# print(sys.argv)
# print(len(sys.argv))
# if len(sys.argv) < 2:
#     sys.argv.append(input("Seu nome: "))

# for nome in sys.argv[1]:
#     print('Olá ', nome)

caminho = sys.argv("C:\Users\20252014050023\OneDrive\Imagens\Camera Roll")
print(caminho)