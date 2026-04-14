import hashlib
nome = str(input('Informe a mensagem: ')) # Sol
num = int(input('Informe a quantidade de bits zero: ')) # 4
nonce = 0
zeros = '0' * (num // 4) # Cria uma string com vários zeros (1 digito hexadecimal é igual a 4 bits).
while True:
    hash = hashlib.sha256(nonce.to_bytes(4, 'big') + nome.encode('utf-8')).digest() # Criação do hash com o nonce de 4 bytes e a mensagem em bytes também.
    hashH = hash.hex() # Converte o hash (que é do tipo bytes) para string
    if hashH.startswith(zeros): # Verifica se o hash começa com a quantidade de zeros desejado.
        print('Nonce encontrado: ', nonce) # print do nonce
        print('Hash: ', hashH) # print do hash
        break
    else: # Se não é igual
        nonce += 1  # O nonce é acrescido mais 1