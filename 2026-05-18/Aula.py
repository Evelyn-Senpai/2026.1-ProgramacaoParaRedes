import base64
# Texto a ser codificado
texto = "Olá mundo!"
# Codificação para Base64
texto_codificado = base64.b64encode(texto.encode('utf-8'))
print("Texto codificado:", texto_codificado.decode('utf-8'))
# Decodificação para texto original
texto_decodificado = base64.b64decode(texto_codificado).decode('utf-8')
print("Texto decodificado:", texto_decodificado)
