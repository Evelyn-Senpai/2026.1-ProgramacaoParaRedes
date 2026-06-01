import socket
from config import *

def get_my_ip10():
    return [addr[4][0] 
        for addr in socket.getaddrinfo(socket.gethostname(), 80) 
            if addr[4][0].startswith('10.')][0]

my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_ip = get_my_ip10()

print(f'Escutando em ({my_ip}:{PORT})')

my_sock.bind((my_ip, PORT))

clientes = []

msg = b''
while msg != END:
    msg, source = my_sock.recvfrom(512)

    if source not in clientes:
        clientes.append(source)

    print(f'Recebi/devolvendo a {source}:{msg}')

    my_sock.sendto(msg, source)

print(f'Recebi fim. Servidor encerrado.')    
my_sock.close()
