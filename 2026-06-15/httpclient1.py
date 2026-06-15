import sys # Importe do sys para chamar o arquivo na linha de comando.
from socket import * # Importe do socket.

def get_data(site, resource, output): # Função que vai buscar o link e tratar do arquivo.
    my_sock = socket(AF_INET, SOCK_STREAM) # Conexão do socket.

    my_sock.connect((site, 80)) # Conexão do link do site com a porta (pode ser qualquer uma).

    request = (f'GET {resource} HTTP/1.1\r\n'
               f'Host: {site}\r\n'
               '\r\n') # Montagem da requisição HTTP.

    my_sock.send(request.encode()) # Transforma o request em bytes.

    data = my_sock.recv(4096) # É pego 4096 bytes do arquivo.
    pos2NL = data.find(b'\r\n\r\n') # Busca por duas quebras de linha (que significa o final do arquivo).
    headers = data[:pos2NL].split(b'\r\n') # É pego o que vem antes do fim do arquivo, ou seja, os headers.

    len_data = -1 # Variável que define o valor inicial do Content-Length.
 
    chunked = False # Variável para localizar o chunked.

    for header in headers[1:]: # Enquanto na primeira parte do header.
        header = header.split(b':', 1) # Separa onde tem ":".
        if header[0] == b'Content-Length': # Se na primeira possição desse header for Content-Length.
            len_data = int(header[1].strip()) # len_data recebe o valor inteiro do Content-Lenght?

        elif header[0] == b'Transfer-Encoding': # Se não, se tiver transfer-Encoding.
            if b'chunked' in header[1]: # E na primeira possição tiver chunked.
                chunked = True # A variável chunked recebe verdadeiro.

    if len_data != -1: # Enquanto len_data for diferente de -1.
        print(f'tamanho dos dados: {len_data}') # Print do tamanho do arquivo.
        data = data[pos2NL+4:] # data recebe os dados do arquivo.
        while len(data) < len_data: # Enquanto o tamanho dos dados for menor que len_data, ou seja, se len_data for maior que 4096 vai continuar.
            data += my_sock.recv(4096) # data recebe os 4096 bytes do arquivo.

        fd = open(output, 'wb') # O arquivo é aberto
        fd.write(data) # É escrito os bytes no arquivo.
        fd.close() # Fechamento do arquivo.
        print(f'Arquivo salvo em {output}') # Print do arquivo salvo.

    elif chunked: # Se não, se chunked é verdadeiro.
        body = data[pos2NL+4:] # body recebe todos blocos.

        fd = open(output, 'wb') # O arquivo é aberto.

        total_bytes = 0 # Variável para armazenar o tamanho total do arquivo.

        while True: # Enquanto for verdade.
            while b'\r\n' not in body: # Enquanto não houver quebra de linha no bloco, ou seja, ainda há dados.
                body += my_sock.recv(4096) # body continua recebendo os dados.

            pos = body.find(b'\r\n') # Busca uma quebra de linha no bloco.

            tamanho_hex = body[:pos] # O tamanho do bloco.
            tamanho = int(tamanho_hex, 16) # O tamanho do bloco como um inteiro.

            if tamanho == 0: # Se o tamanho for 0, ou seja, não há próximo chunk.
                break # O programa para.

            chunk = body[pos+2:] # chunk recebe os dados do bloco

            while len(chunk) < tamanho + 2: # Garante que o bloco chegou inteiro.
                chunk += my_sock.recv(4096) # chunk recebe os 4096 bytes do bloco.

            fd.write(chunk[:tamanho]) # É escrito os dados do bloco no arquivo.

            total_bytes += tamanho # total_bytes recebe o tamanho desse bloco.

            body = chunk[tamanho+2:] # Recebe o próximo bloco.

        fd.close() # Fechamento do arquivo
        print(f'tamanho dos dados: {total_bytes}') # Print do tamanho do arquivo.
        print(f'Arquivo salvo em {output}') # Print do arquivo salvo.

    my_sock.close() # Encerramento da conexão.

if len(sys.argv) == 4: # Se houver 4 argumentos na linha de comando.
    get_data(sys.argv[1], sys.argv[2], sys.argv[3]) # A função é chamada com esses quatro argumentos.

else: # Se não.
    print('uso: python site resouce output_filename')
    print('Exemplos:') # Exemplo de como se deve fazer. 
    print(' python httpclient1.py httpbin.org /image/png porco.png')
    print(' python httpclient1.py httpbin.org /image/jpeg lobo.jpg')
    print(' python httpclient1.py viacep.com.br /ws/59062570/json/ meucep.json')
    print(' python httpclient1.py viacep.com.br /ws/Rn/Natal/Silva ruassilva.json')
