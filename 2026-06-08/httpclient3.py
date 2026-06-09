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
    for header in headers[1:]:
        header = header.split(b':')
        if header[0] == b'Content-Length':
            len_data = int(header[1])

    if len_data != -1:
        print(f'tamanho dos dados: {len_data}')
        data = data[pos2NL+4:]
        while len(data) < len_data:
            data += my_sock.recv(4096)

        fd = open(output, 'wb')
        fd.write(data)
        fd.close()
        print(f'Arquivo salvo em {output}')

    else:
        print('Content-Length não encontrado!')
        print('Transferência baseado em chunks não implementado (ainda)!')
        my_sock.close()

if len(sys.argv) == 4:
    get_data(sys.argv[1], sys.argv[2], sys.argv[3])

else:
    print('uso: python site resouce output_filename')
    print('Exemplos:')
    print(' python httpclient3.py httpbin.org /image/png porco.png')
    print(' python httpclient3.py viacep.com.br /ws/59062570/json/ meucep.json')
    print(' python httpclient3.py httpbin.org /image/jpeg lobo.jpg')

