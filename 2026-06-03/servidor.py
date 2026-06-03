import socket

SERVER_FILES="server_files/"
my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_sock.bind (('127.0.0.1', 12346))

while True:
    # Le do cliente o nome do arquivo
    file_name, source = my_sock.recvfrom(512)
    if file_name == b'Sair':
        print('Servidor encerrado.')
        break
    fd = open (SERVER_FILES+file_name.decode(), "rb")
    while True:
        bloco = fd.read(1024)
        if not bloco:
            break
        my_sock.sendto(bloco, source)
    fd.close()

    my_sock.sendto(b'Sair', source)
my_sock.close()