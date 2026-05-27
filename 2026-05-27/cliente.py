import socket
from config import *

my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = input("IP/nome do servidor: ")

msg = b''
while msg != END:
    msg = input('Mensagem: ').encode()

    if msg:
        print(f'Enviando: {msg}')

        my_sock.sendto(msg, (server_ip, PORT))

        answer, source = my_sock.recvfrom(512)

        print(f'Recebido de {source}: {answer.decode('utf-8')}')

print(f'Digitado {END.decode('utf-8')}. Cliente encerrado.')
my_sock.close()
