import socket

SERVER_FILES="server_files/"
my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_sock.bind (('127.0.0.1', 12346))

while True:
    # Le do cliente o nome do arquivo
    file_name, source = my_sock.recvfrom(512)
    fd = open (SERVER_FILES+file_name.decode(), "rb")
    # Indo para o final do arquivo
    pos_final = fd.seek(0, 2)
    tamanho =  pos_final.to_bytes(4, 'big')
    my_sock.sendto(tamanho, source)
    # Voltando para o inicio do arquivo
    fd.seek(0, 0)
    data = fd.read(1024)
    total = 0
    while data != b'':
        my_sock.sendto(data, source)
        total += len(data)
        my_sock.close()
