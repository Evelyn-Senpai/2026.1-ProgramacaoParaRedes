import socket

def get_my_ip10():
    return [addr[4][0] 
        for addr in socket.getaddrinfo(socket.gethostname(), 80) 
            if addr[4][0].startswith('10.')][0]

SERVER_FILES = "server_files/"

my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

my_ip = get_my_ip10()

my_sock.bind((my_ip, 12345))

while True:
    file_name, source = my_sock.recvfrom(512)

    fd = open(SERVER_FILES+file_name, 'rb')

    buffer = fd.read()

    fd.close()
    