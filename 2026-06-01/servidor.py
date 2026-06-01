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

clientes = set()

msg = b''
while msg != END:
    msg, source = my_sock.recvfrom(512)

    clientes.update({source})

    for cliente in clientes:
        if cliente != source:
            my_sock.sendto(msg, source)

print(f'Recebi {END}. Servidor encerrado.')    
my_sock.close()
