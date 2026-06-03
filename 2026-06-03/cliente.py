import socket

CLIENT_FILES="client_files/"
SERVER = ("127.0.0.1", 12346)
my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    file_name = input("Nome do arquivo a baixar: ")
    if file_name == "Sair":
        my_sock.sendto(b'Sair', SERVER)
        print('Cliente encerrado.')
        break
    my_sock.sendto(file_name.encode(), SERVER)

    fd = open (CLIENT_FILES+file_name, "wb")
    while True:
        data, source = my_sock.recvfrom(1024)
        if data == b'Sair':
            break
        fd.write(data)
    fd.close()
    print('Download concluído.')