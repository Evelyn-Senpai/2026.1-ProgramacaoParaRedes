n = 384
#  Ver os bytes de um inteiro
nBytes = n.to_bytes(4, "big")
print(nBytes)
#  Converter os bytes para inteiro
bN = int.from_bytes(nBytes, "big")
print(bN)