import hashlib
nome = str(input('Informe a mensagem: '))
num = int(input('Informe a quantidade de bits zero: '))
nonce = 0 # Contador
while True:
    hash = hashlib.sha256(nonce.to_bytes(4, 'big') + nome.encode('utf-8')).digest() # Criação do hash com o nonce de 4 bytes junto da mensagem em bytes também.
    if (int.from_bytes(hash, 'big') >> (256 - num)) == 0: # Primeiro: Converte o hash em um número inteiro, Segundo: O hash tem 256 bits, então é subtraido 256 de num (a quantidade de zeros desejado), o resultado são os primeiro bits do hash que são num. Se isso for verdade, é encontrado o nonce do hash.
        print('Nonce encontrado: ', nonce) # print do nonce.
        print('Hash: ', hash) # print do hash.
        break
    else: # Se não é igual.
        nonce += 1  # O nonce é acrescido mais 1.