import socket

PORT = 12345
IP = "127.0.0.1"

my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_ip = socket.gethostbyname(socket.gethostname())

print(f'Escutando em ({my_ip}:{PORT})')

my_sock.bind((my_ip, PORT))

while True:
    msg, source = my_sock.recvfrom(512)

    if msg:
        print(f'Recebi/devolvendo a {source}: {msg}')

        my_sock.sendto(msg, source)
    
    else:
        print('Servidor encerrado.')

        break

my_sock.close()
