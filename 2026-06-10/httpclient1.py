import sys
from socket import *

def get_data(site, resouce, output):
    my_sock = socket(AF_INET, SOCK_STREAM)

    my_sock.connect((site, 80))

    request = (f'GET {resouce} HTTP/1.1\r\n'
               f'Host: {site}\r\n'
               '\r\n')

    my_sock.send(request.encode())

    data = my_sock.recv(4096)
    pos2NL = data.find(b'\r\n\r\n')
    headers = data[:pos2NL].split(b'\r\n')

    len_data = -1

    chunked = False 

    for header in headers[1:]:
        header = header.split(b':', 1)
        if header[0] == b'Content-Length':
            len_data = int(header[1].strip())

        elif header[0] == b'Transfer-Encoding':
            if b'chunked' in header[1]:
                chunked = True

    if len_data != -1:
        print(f'tamanho dos dados: {len_data}')
        data = data[pos2NL+4:]
        while len(data) < len_data:
            data += my_sock.recv(4096)

        fd = open(output, 'wb')
        fd.write(data)
        fd.close()
        print(f'Arquivo salvo em {output}')

    elif chunked:
        body = data[pos2NL+4:]

        fd = open(output, 'wb')

        total_bytes = 0

        while True:
            while b'\r\n' not in body:
                body += my_sock.recv(4096)

            pos = body.find(b'\r\n')

            tamanho_hex = body[:pos]
            tamanho = int(tamanho_hex, 16)

            if tamanho == 0:
                break

            body = body[pos+2:]

            while len(body) < tamanho + 2:
                body += my_sock.recv(4096)

            fd.write(body[:tamanho])

            total_bytes += tamanho

            body = body[tamanho+2:]

        fd.close()
        print(f'tamanho dos dados: {total_bytes}')
        print(f'Arquivo salvo em {output}')

    my_sock.close()

if len(sys.argv) == 4:
    get_data(sys.argv[1], sys.argv[2], sys.argv[3])

else:
    print('uso: python site resouce output_filename')
    print('Exemplos:')
    print(' python httpclient1.py httpbin.org /image/png porco.png')
    print(' python httpclient1.py viacep.com.br /ws/59062570/json/ meucep.json')
    print(' python httpclient1.py httpbin.org /image/jpeg lobo.jpg')

