import socket

# Conexão
# Família -> IPv4, Protocolo -> UDP (SOCK_STREAM -> TCP)
so = socket(socket.AF_INET, socket.SOCK_DGRAM)

# Acoplação da máquina local
so.bind(('localhost', 80))

# Fecha a conexão
so.close()

'''Exemplo 01'''
# Um cliente UDP
import socket
HOST = '10.20.1.171' #Definindo o IP do servidor
PORT = 50000 #Definindo a porta
# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input('Digite a mensagem: ')
# Convertendo a mensagem digitada de string para bytes
msg = msg.encode('utf-8')
# Enviando a mensagem ao servidor
udp_socket.sendto(msg, (HOST, PORT))
# Fechando o socket
udp_socket.close()

# Um servidor UDP
import socket
HOST = ''  #Definindo o IP do servidor
PORT = 50000 #Definindo a porta
# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, PORT)) # Ligando o socket a porta
print('Recebendo Mensagens...\n\n')
while True:
    # Recebendo os dados do cliente
    msg, cliente = udp_socket.recvfrom(512) #buffer de 512 bytes
    # Imprimindo a mensagem recebida convertendo de bytes para string
    print(cliente, msg.decode('utf-8'))
    break
# Fechando o socket
udp_socket.close()

'''Exemplo 02'''
# Um cliente TCP
import socket
HOST = '10.20.1.171' #Definindo o IP do servidor
PORT = 50000 #Definindo a porta
# Criando o socket UDP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((HOST, PORT)) # Ligando o socket a porta
msg = input('Digite a mensagem: ')
# Convertendo a mensagem digitada de string para bytes
msg = msg.encode('utf-8')
# Enviando a mensagem ao servidor
tcp_socket.send(msg)
# Fechando o socket
tcp_socket.close()

# Um servidor TCP
import socket
HOST = ''  #Definindo o IP do servidor
PORT = 50000 #Definindo a porta
# Criando o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((HOST, PORT)) # Ligando o socket a porta
tcp_socket.listen(1) # Máximo de conexões enfileiradas
print('Recebendo Mensagens...\n\n')
while True:
    con, cliente = tcp_socket.accept() # Aceita a conexão com o cliente
    print('Conectado por: ', cliente)
    while True:
        msg = con.recv(1024) #buffer de 1024 bytes
        if not msg: break
        # Imprimindo a mensagem recebida convertendo de bytes para string
        print(cliente, msg[0].decode('utf-8'))
    print('Finalizando Conexão do Cliente ', cliente)
    con.close()