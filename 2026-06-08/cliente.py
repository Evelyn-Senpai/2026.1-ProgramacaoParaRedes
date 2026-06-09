# Importando a biblioteca socket
import socket

def get_my_ip10():
    return [addr[4][0] 
         for addr in socket.getaddrinfo(socket.gethostname(), 80) 
             if addr[4][0].startswith('10.')
        ][0]

HOST = get_my_ip10() # Definindo o IP do servidor
PORT = 50000 # Definindo a porta

# Criando o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect((HOST, PORT))

msg = input('Digite a mensagem: ')
# Convertendo a mensagem digitada de string para bytes
msg = msg.encode('utf-8')

# Enviando a mensagem ao servidor
tcp_socket.send(msg)

# Fechando o socket
tcp_socket.close()