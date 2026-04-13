'''Faça um programa que lê um arquivo e uma palavra chave e gera um arquivo cifrado com cada byte
sendo um XOR com um byte da palavra chave.'''

# import os

# diretorio = os.path.dirname(__file__)
# nomeArquivo = input("Digite o nome do arquivo: ")
# palavraChave = input("Digite a palavra chave: ")
# arquivo = f'{nomeArquivo}.txt'
# open(f'{diretorio}\\{arquivo}', 'w').close()
# open(f'{diretorio}\\{arquivo}', 'a')
# arquivo.write(palavraChave)
# arquivo.close()










import os
import sys

if __name__ == '__main__':
    diretorio = os.path.dirname(__file__)

    nome_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip()
    if not nome_arquivo:
        print("Nome do arquivo não pode estar vazio.")
        sys.exit(1)

    palavra_chave = input("Digite a palavra chave: ").strip()
    if not palavra_chave:
        print("A palavra chave não pode estar vazia.")
        sys.exit(1)

    arquivo_entrada = f"{nome_arquivo}.txt"
    caminho_entrada = os.path.join(diretorio, arquivo_entrada)

    if not os.path.isfile(caminho_entrada):
        print(f"Arquivo '{arquivo_entrada}' não encontrado no diretório do script.")
        sys.exit(1)

    with open(caminho_entrada, 'rb') as f:
        dados = f.read()

    chave_bytes = palavra_chave.encode('utf-8')
    dados_cifrados = bytearray(len(dados))
    for i, byte in enumerate(dados):
        dados_cifrados[i] = byte ^ chave_bytes[i % len(chave_bytes)]

    arquivo_saida = f"{nome_arquivo}_cifrado.txt"
    caminho_saida = os.path.join(diretorio, arquivo_saida)
    with open(caminho_saida, 'wb') as f:
        f.write(dados_cifrados)

    print(f"Arquivo cifrado gerado: {arquivo_saida}")
