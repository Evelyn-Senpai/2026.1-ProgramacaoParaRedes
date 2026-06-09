# Importando a biblioteca socket
import socket

HOST = '' # Definindo o IP do servidor
PORT = 50000 # Definindo a porta

# Criando o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.bind((HOST, PORT)) # Ligando o socket a porta
tcp_socket.listen(1) # Máximo de conexões enfileiradas

print('Recebendo Mensagens...\n\n')

while True:
    con, cliente = tcp_socket.accept() # Aceita a conexão com o cliente
    print('Conectado por: ', cliente)
    while True:
        msg = con.recv(1024) # Buffer de 1024 bytes
        if not msg: break
        # Imprimindo a mensagem recebida convertendo de bytes para string
        print(cliente, msg.decode('utf-8'))

    print('Finalizando Conexão do Cliente ', cliente)
    con.close()
    