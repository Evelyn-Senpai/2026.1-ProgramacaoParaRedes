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

imagens = os.listdir(pasta) # Uma lista das imagem que estão na pasta.

coordenadas = [] # Lista para guardar as coordenadas das imagens.

for imagem in imagens: # Pega cada nome de cada uma das imagens.
    caminho = os.path.join(pasta, imagem) # Pega o caminho que a imagem está, ou seja, pega a imagem.

    abreImagem = open(caminho, 'rb') # Abre em formatado de bytes.

    cabImagem = abreImagem.read(4) # Lê os quatro primeiros bytes da imagem.

    idImagem = cabImagem[0:2] # Pega os dois primeiros bytes do cabImagem, o identificador para saber se a imagem é JPEG.

    idMetadados = cabImagem[2:4] # Pega os dois últimos bytes do cabImagem, o identificador para saber se os metadados da imagem são EXIF.

    if idImagem == b'\xff\xd8': # Verifica se a imagem é JPEG.
        if idMetadados == b'\xff\xe1': # Se a imagem for JPEG, verifica se os metadados da imagem são EXIF.
            tamSecao = int.from_bytes(abreImagem.read(2), 'big') # Lê os dois bytes após o cabImagem que identifica o tamanho da seção e converte para um número inteiro.

            exif = abreImagem.read(6) # Lê os seis bytes após o tamanho da seção que identifica o EXIF header, que são valores fixos.

            inicioTIFF = abreImagem.tell() # Para salvar a atual posição do ponteiro na imagem.

            tiff = abreImagem.read(8) # Lê os próximos oito bytes que identifica o TIFF header.
            endianess = tiff[:2] # Pega os primeiros bytes do TIFF header que identificam como se deve tratar os grupos de bytes, big ou little endian.
            if endianess == b'\x49\x49': # Verifica se o endianess é little endian.
                endian = 'little'
            else: # Se não for little endian, é big endian.
                endian = 'big'

            nMetadados = int.from_bytes(abreImagem.read(2), endian) # Lê os próximos dois bytes que identificam o número de metadados, e converte para um valor inteiro.

            for metadados in range(nMetadados): # Para cada bloco de metadados.
                metadado = abreImagem.read(12) # Lê a cada doze bytes que é um bloco de metadado.

                idMetadado = int.from_bytes(metadado[0:2], endian) # Pega o id do metadado que identifica qual informação aquele metadado guarda.
                if idMetadado == 34853: # Se o id do metadados for esse, quer dizer que é uma informação de GPS>
                    gps = int.from_bytes(metadado[8:12], endian) # Pega a posição do bloco GPS e converte para um valor inteiro.
                    
                    abreImagem.seek(inicioTIFF + gps) # Pula para onde começa os dados GPS.

                    nGPS = int.from_bytes(abreImagem.read(2), endian) # Lê os dois primeiros bytes dos metadados GPS que identificam o número de metadados GPS e converte para um número inteiro.
                    
                    latitude = None # Se latitude não existir vai ter o valor None.
                    longitude = None # Se longitude não existir vai ter o valor None.

                    for metadadosGPS in range(nGPS): # Para os metadados GPS.
                        metadadoGPS = abreImagem.read(12) # Lê cada metadado GPS.

                        idmetadadoGPS = int.from_bytes(metadadoGPS[0:2], endian) # Pega os primeiros dois bytes do metadadoGPS que identifica o id do metadaoGPS e converte para um número inteiro.
                        if idmetadadoGPS == 2: # identifica Latitude.
                            offsetLatitude = int.from_bytes(metadadoGPS[8:12], endian) # Pega onde está latitude.

                            posicaoAtual = abreImagem.tell() # Para salvar a atual posição do ponteiro na imagem.

                            abreImagem.seek(inicioTIFF + offsetLatitude) # Pula até essa posição.

                            dadosLatitude = abreImagem.read(24) # Lê os 24 bytes onde estão as informações da latitude.

                            grausN = int.from_bytes(dadosLatitude[0:4], endian) # Pega os primeiros quatro bytes dos dados da latitude que identificam o numerador dos graus.
                            grausD = int.from_bytes(dadosLatitude[4:8], endian) # Pega mais quatro bytes dos dados da latitude que identificam o denominador dos graus.
                            graus = grausN / grausD # Divide o numerador pelo denominador que vai ser o valor real.

                            minN = int.from_bytes(dadosLatitude[8:12], endian) # Pega os quatro próximos bytes dos dados da latitude que identificam o numerador dos minutos.
                            minD = int.from_bytes(dadosLatitude[12:16], endian) # Pega os quatro próximos bytes dos dados da latitude que identificam o denominador dos minutos.
                            minutos = minN / minD # Divide o numerador pelo denominador que vai ser o valor real.                             

                            segN = int.from_bytes(dadosLatitude[16:20], endian) # Pega os quatro próximos bytes dos dados da latitude que identificam o numerador dos segundos.
                            segD = int.from_bytes(dadosLatitude[20:24], endian) # Pega os quatro próximos bytes dos dados da latitude que identificam o denominador dos segundos.
                            segundos = segN / segD # Divide o numerador pelo denominador que vai ser o valor real.
                        
                            latitude = graus + (minutos / 60) + (segundos / 3600) # Cálculo da latitude.

                            abreImagem.seek(posicaoAtual) # Volta para a posição anterior para continuar o loop.

                        elif idmetadadoGPS == 4:
                            offsetLongitude = int.from_bytes(metadadoGPS[8:12], endian) # Pega onde está longitude.

                            posicaoAtual = abreImagem.tell() # Para salvar a atual posição do ponteiro na imagem.

                            abreImagem.seek(inicioTIFF + offsetLongitude) # Pula até essa posição.

                            dadosLongitude = abreImagem.read(24) # Lê os 24 bytes onde estão as informações da longitude.

                            grausN = int.from_bytes(dadosLongitude[0:4], endian) # Pega os primeiros quatro bytes dos dados da longitude que identificam o numerador dos graus.
                            grausD = int.from_bytes(dadosLongitude[4:8], endian) # Pega mais quatro bytes dos dados da longitude que identificam o denominador dos graus.
                            graus = grausN / grausD # Divide o numerador pelo denominador que vai ser o valor real.

                            minN = int.from_bytes(dadosLongitude[8:12], endian) # Pega os quatro próximos bytes dos dados da longitude que identificam o numerador dos minutos.
                            minD = int.from_bytes(dadosLongitude[12:16], endian) # Pega os quatro próximos bytes dos dados da longitude que identificam o denominador dos minutos.
                            minutos = minN / minD # Divide o numerador pelo denominador que vai ser o valor real.                             

                            segN = int.from_bytes(dadosLongitude[16:20], endian) # Pega os quatro próximos bytes dos dados da longitude que identificam o numerador dos segundos.
                            segD = int.from_bytes(dadosLongitude[20:24], endian) # Pega os quatro próximos bytes dos dados da longitude que identificam o denominador dos segundos.
                            segundos = segN / segD # Divide o numerador pelo denominador que vai ser o valor real.

                            longitude = graus + (minutos / 60) + (segundos / 3600) # Cálculo da longitude.
                    
                            abreImagem.seek(posicaoAtual) # Volta para a posição anterior para continuar o loop.
                    
                    if latitude is not None and longitude is not None: # Se os valores de latitude e longitude não forem vazios.
                        coordenadas.append((latitude, longitude)) # A lista coordenadas recebe a latitude e a longitude de cada imagem.

    abreImagem.close() # Fechamento da imagem.

url = 'https://www.google.com/maps/dir/' # Para criar a URL.

for latitude, longitude in coordenadas[:10]: # Pega os dez primeiras coordenadas na lista.
    url += f'{latitude:.6f},{longitude:.6f}/' # Adiciona as coordenadas na URL.

print(url) # Print da URL.
