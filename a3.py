'''
## Simulação de RAID (50 pontos)

<hr/>

A tecnologia **RAID** (*Redundant Array of Inexpensive Disks*) é sido muito empregada em datacenters como meio de obter discos de grande capacidade a partir de discos convencionais. Existem vários níveis de RAID. 

No mais simples dos níveis de RAID, vários discos são combinados para ao final obter a capacidade agregada dos discos, como sendo oriunda de um só disco. A implementação da tecnologia é mais comum usando *hardware*, mas os sistemas operacionais mais populares disponibilizam implementações em software. 

Para entender o RAID nível 0 (ou **RAID0**), considere que dois discos de 10 KB estão disponíveis e deseja-se obter um disco de 20 KB. Isso é possível dividindo cada disco em dez blocos de 1 KB. Nesse cenário as organizações físicas e lógicas estão representadas na figura seguinte.

<img width="688" height="233" alt="fig1" src="https://github.com/user-attachments/assets/4132e0a7-79b8-4a0e-8e86-1e8a2b98a763" />

Assim, os dois discos são considerados como um só disco lógico. Quando for solicitada a leitura (ou escrita) de dados na posição 14750, por exemplo, o sistema os recupera no bloco lógico 14, que em termos físicos, corresponde ao bloco 4 do disco 1.

No nível 5 (**RAID5**) a lógica é mais complexa, pois permite recuperar dados em caso de um dos discos do *array* apresentar falha. Além disso, ao invés de numerar todos os blocos sequencialmente do disco 0 e depois usar o disco 1, eles são utilizados alternadamente. 

Antes de compreender todos os detalhes do **RAID5**, considere o **RAID4** que é uma simplificação daquele. Na Figura seguinte estão quatro discos em **RAID4**, já na estrutura lógica.

<img width="642" height="233" alt="fig2" src="https://github.com/user-attachments/assets/192f5f1a-818e-46f8-993e-7d50354dfd7d" />

Existem no **RAID4** duas mudanças muito relevantes em relação ao RAID0.
- Os blocos não são alocados completamente no disco 0, para depois alocar no disco 1 e nos demais discos. Eles estão alocados na *horizontal*, ou seja, aloca-se o bloco 0 no disco 0, e um bloco em cada um dos discos subsequentes, até todos os discos tenham um bloco. A seguir o disco 0 recebe um novo bloco e o processo se repete.
- O último disco é denominado de disco de paridade e não armazena blocos de dados, mas blocos que contemplam a operação *xor* entre os bytes em cada um dos blocos de dados na posição correspondente. Considerando que cada bloco tem 1KB, o primeiro byte do bloco 0 do disco 3 é um xor dos primeiros bytes nos blocos 0, 1 e 2 (nos discos 0, 1 e 2). O segundo byte do boco 0 no disco 3 é um xor dos segundos bytes nos blocos 0, 1 e 2 (nos discos 0, 1 e 2). Como um exemplo geral, o byte 20 do bloco 5 do disco 3 é um xor dos bytes nas posições 20 dos blocos 15, 16 e 17 (nos discos 0, 1 e 2).

A estratégia do RAID4 é tal que se um dos discos com dados for perdido, os seus dados ainda podem ser recuperados, mediante a operação de *xor* entre os discos de dados remanescentes e o disco de paridade. A operação de recuperação é a mesma utilizada para gerar os dados de paridade, só que nesse caso utiliza-se os valores nele armazenados para obter os dados do disco defeituoso.

Com base nessa explicação, desenvolva um programa que simula o comportamento do **RAID4**. Inicie criando as funções, apresentadas como operações ao ao usuário em um menu:

- ```inicializaRAID```	Pergunta ao usuário quantos discos serão utilizados em **RAID4**, o tamanho dos discos (o mesmo para todos) e o tamanho do bloco. Os arquivos devem ser criados em uma pasta que o usuário também deve informar.
Essa função deve criar um arquivo para cada um dos discos (disco0.bin, disco1.bin, disco2.bin, .... discoX.bin). O arquivo discoX.bin representa o disco de paridade (X é antecessor do número de discos informado pelo usuário). Cada arquivo representando discos de dados deve ter todo o seu conteúdo zerado, enquanto o arquivo que guarda o disco de paridade deve ter os dados calculados pela aplicação do xor dos arquivos de dados.
- ```obtemRAID```	Essa operação pergunta ao usuário as mesmas informações de ```InicializaRAID```, mas em vez criar os arquivos, busca aqueles criados anteriormente com inicializaRAID. Se algum dos discos estiver ausente, o programa deve seguir normalmente. Se mais de um estiver ausente, indique a impossibilidade e saia do programa.
- ```reconstroiRAID``` Recria um disco ausente, se for o caso. Um novo arquivo deve ser criado e ter seu conteúdo gerado a partir dos arquivos correspondes aos discos remanescentes e ao disco de paridade.
- ```escreveRAID``` Pergunta ao usuário um conjunto de dados a gravar no *RAID* e a posição onde iniciar a gravação. Essa posição pode ser qualquer valor entre zero e o tamanho lógico do RAID -1. Por exemplo, se o RAID tem cinco discos (quatro de dados e um de paridade) e o tamanho dos discos é 10000 bytes, então a posição pode ser qualquer valor entre 0 e 39999. O programa deve identificar em que arquivo(s) gravar os dados e que posição dentro do(s) arquivo(s). Após a escrita no arquivo correto, o disco de paridade deve ser atualizado.
- ```leRAID``` Pergunta ao usuário informações sobre dados a ler do RAID. O usuário informa a posição e quantos bytes ler. A lógica para encontrar o arquivo de onde ler é a mesma da escrita.  A paridade não necessita ser atualizada.
- ```removeDiscoRAID``` O usuário indica um disco a remover do **RAID4** (simulando um defeito). O arquivo que representa o disco deve ser apagado pelo programa. Ainda assim, as operações seguintes de leitura e escrita devem operar normalmente, mesmo quando envolvem o disco removido. 
Quando a leitura envolve o disco removido, os dados devem ser obtidos mediante *xor* nos demais discos e no disco de paridade. A operação de escrita no disco removido gera efeitos apenas no disco de paridade, a fim de permitir (indiretamente) que os dados sendo gravados possam ser recuperados em futuras leituras.

Procure desenvolver o programa com uma ou mais funções para implementar cada uma das funcionalidades. No início, considere que as leituras/escritas não ultrapassam limites de bloco. Na segunda versão, implemente completamente. 

Algumas dicas:
- As operações nos arquivos envolvem leitura/escrita de dados em formato binário, portanto devem ser abertos no modo “ab+” (leia a documentação da função open, ou simplesmente digite ```help(open)``` no interpretador).
- Use extensivamente a função ```seek``` para localizar as posições de leitura/escrita nos arquivos que simulam os discos.

Por fim, o funcionamento do **RAID5** é similar ao **RAID4**. No entanto, a fim de evitar sobrecarga no disco de paridade, haja vista que qualquer escrita em um dos discos de dados implica em escrever o disco de paridade também, no **RAID5** a paridade é gravada uniformemente em todos os discos, conforme representado na Figura seguinte.

<img width="692" height="251" alt="fig3" src="https://github.com/user-attachments/assets/b90f0e1c-b45d-4c64-bb6f-a9fbe1b2f7d2" />

Opcionalmente, faça uma nova ver são do programa, mas agora usando o **RAID5** (10 bônus por esse desenvolvimento).
                                
										   
Faça uma nova versão do programa, mas agora usando o RAID5
'''

'''
## RAID4

import os

def inicializaRAID(q, t, p): # Função que cria e armazena os discos. 
    for i in range(0, q-1): # De acordo com a quantidade de discos informados, menos um, porque o último disco tem que ser o de paridade.
        caminho = os.path.join(p, f'disco{i}.bin') # Pega o caminho que está a pasta para criar o disco.
        
        disco = open(caminho, 'wb+') # Abre/cria o disco em formato de bytes.
        disco.write(b'\x00' * t) # Escreve no disco de acordo com o tamanho informado.
        disco.close() # Fecha o disco.

        print(f'- disco{i}.bin criado com sucesso.') # Print do disco que foi criado com sucesso.
    
    discoParidade = os.path.join(p, f'discoX.bin') # Cria o disco de paridade, já no caminho correto.
    paridade = bytearray(t) # Um array vazio com o tamanho que foi informado para os discos que foram digitados.

    discos = os.listdir(p) # Uma lista dos discos que estão na pasta.
    for disco in discos: # Em cada nome do disco.
        if disco != 'discoX.bin': # Se o disco não for o de paridade, porque o disco de paridade não entra no cálculo da própria paridade.
            caminho = os.path.join(p, disco) # Pega o caminho que o disco está, ou seja, pega o disco.

            abreDisco = open(caminho, 'rb') # Abre/cria em formato de bytes.        
            dados = abreDisco.read() # Lê o conteúdo do disco.
            abreDisco.close() # Fechamento do disco existente.

            for i in range(len(dados)): # Em cada byte que está em dados.
                paridade[i] ^= dados[i] # Em cada posição no array de bytes, recebe um xor dos dados de cada disco naquela posição. 

    abreParidade = open(discoParidade, 'wb') # Abre/cria o disco de paridade.
    abreParidade.write(paridade) # Escreve a paridade no disco de paridade.
    abreParidade.close() # Fecha o disco de paridade.

    print(f'- discoX.bin criado com sucesso.') # Print do disco de paridade que foi criado com sucesso.

def obtemRAID(q, p): # Função para verificar os discos criados.
    discos = os.listdir(p) # Uma lista dos discos que estão na pasta.
    
    ausentes = 0 # Para contar quantos discos estão ausentes.

    for i in range(q-1): # De acordo com a quantidade informada.
        if f'disco{i}.bin' in discos: # Se o disco estiver na lista da pasta de discos.
            print(f'- disco{i}.bin presente.') # Print do disco que está presente.
        
        else: # Se o disco estiver ausente.
            print(f'- disco{i}.bin ausente.') # Print do disco que está ausente, ou seja, que deveria ter sido criado.
            
            ausentes += 1 # Se o disco estiver ausente, o contador recebe mais um.

    if f'discoX.bin' in discos: # Se o disco de paridade estiver na lista da pasta de discos.
        print(f'- discoX.bin presente.') # Print do disco de paridade que está presente.
        
    else: # Se o disco de paridade estiver ausente.
        print(f'- discoX.bin ausente.') # Print do disco de paridade que está ausente.
            
        ausentes += 1 # Se o disco estiver ausente, o contador recebe mais um.

    if ausentes >= 2: # Se tiver mais de um disco ausente, o RAID será inválido.
        print('Mais de um disco ausente!\n --- RAID inválido ---') # Print do RAID inválido.
        return # O programa não deve continuar.

    else: # Se não, o RAID será válido.
        print('--- RAID válido ---') # Print do RAID válido.

def reconstroiRAID(q, t, p): # Função para construir um disco ausente.
    discos = os.listdir(p) # Uma lista dos discos que estão na pasta.

    nomeAusente = None # Para guardar o nome do disco ausente.

    for i in range(q-1): # De acordo com a quantidade informada.
        if f'disco{i}.bin' not in discos: # Se o disco não estiver na lista da pasta de discos.
            nomeAusente = f'disco{i}.bin' # Pega o nome do disco que está ausente.       

    if f'discoX.bin' not in discos: # Se o disco de paridade não estiver na lista da pasta de discos.
        nomeAusente = 'discoX.bin' # Pega o nome do disco de paridade que está ausente.

    if nomeAusente is not None: # Se o nomeAusente não estiver vazio, ou seja, tem um disco ausente, ele vai reconstruir o disco.
        caminhoAusente = os.path.join(p, nomeAusente) # Caminho do disco ausente.
        novoDisco= open(caminhoAusente, 'wb') # Abre/cria o novo disco, ou seja, o disco que estava ausente.

        for i in range(t): # Para cada byte do tamanho.
            byteRecuperado = 0 # Cada byte do novo disco, vai ser um byte xor do discoX com outro disco, ou seja, um byte recuperado.

            for disco in discos: # Para cada disco na lista de discos.
                if disco != nomeAusente: # Se não for o novo disco criado.
                    caminho = os.path.join(p, disco) # Pega o caminho que o disco está, ou seja, pega o disco.
                    
                    abreDisco = open(caminho, 'rb') # Abre em formato de bytes.
                    abreDisco.seek(i) # Vai até a posição i, e em posição em posição.
                    
                    byte = abreDisco.read(1) # Lê esse byte.
                    byteRecuperado ^= byte[0] # Byte recuperado recebe o xor do byte.

                    abreDisco.close() # Fechamento do disco existente.

            novoDisco.write(bytes([byteRecuperado])) # Escreve o byte recuperado no novo disco.

        novoDisco.close() # Ao final, fecha o novo disco.

        print(f'{nomeAusente} reconstruído com sucesso.')

def escreveRAID(c, p, q, pd, t): # Função que escreve um conjunto de dados em determinado disco.
    dadoDisco = p % (q-1) # O resto da divisão, da posição pela quantidade de discos, é em qual disco aquela posição está.

    offset = p // (q-1) # A divisão inteira, da posição pela quantidade de discos, para descobrir qual a posição em relação ao disco, ou seja, qual byte do disco representa aquela posição.
    
    caminho = os.path.join(pd, f'disco{dadoDisco}.bin') # Pega o caminho que o disco desejado está.

    if os.path.exists(caminho): # Se o caminho existir.
        abreDisco = open(caminho, 'rb+') # Abre o disco em formato de bytes.
        abreDisco.seek(offset) # Pula para a posição desejada.
        abreDisco.write(c.encode("utf-8")) # Escreve o conjunto de dados, em bytes, na posição.
        abreDisco.close() # Fecha o disco.

        print(f'- Dados inseridos em disco{dadoDisco}.bin com sucesso.') # Print para informar que os dados foram inseridos no disco certo de acordo com a posição informada.

    else: # Se o caminho não existir (caso o disco tenha sido removido).
        print(f'- disco{dadoDisco}.bin está ausente.') # Print para informar que dado disco está ausente.
        print('- Os dados não foram escritos diretamente no disco.') # Print para informar que os dados não foram gravados diretamente no disco (foram para o disco de paridade).

    # Para atualizar o disco de paridade, basicamente é a mesma lógica feita na função inicializaRAID, uma vez que o disco de paridade já foi criado.
    discoParidade = os.path.join(pd, 'discoX.bin') # Pega o caminho do disco de paridade.

    paridade = bytearray(t) # Um array vazio com o tamanho que foi informado para os discos que foram digitados.

    discos = os.listdir(pd) # Uma lista dos discos que estão na pasta.

    for disco in discos: # Em cada nome do disco.
        if disco != 'discoX.bin': # Se o disco não for o de paridade, porque o disco de paridade não entra no cálculo da própria paridade.
            caminho = os.path.join(pd, disco) # Pega o caminho que o disco está, ou seja, pega o disco.

            abreDisco = open(caminho, 'rb') # Abre/cria em formato de bytes.        
            dados = abreDisco.read() # Lê o conteúdo do disco.
            abreDisco.close() # Fechamento do disco existente.

            for i in range(len(dados)): # Em cada byte que está em dados.
                paridade[i] ^= dados[i] # Em cada posição no array de bytes, recebe um xor dos dados de cada disco naquela posição. 

    caminhoDisco = os.path.join(pd, f'disco{dadoDisco}.bin') # Pega o caminho que o disco desejado está.

    if not os.path.exists(caminhoDisco): # Se o caminho não existe, ou seja, o disco que não exite não era o disco de paridade.
        dadosNovos = c.encode("utf-8") # Transforma o conjunto de dados em bytes.

        for i in range(len(dadosNovos)): # Enquanto no tamanho do conjunto de dados que deseja ser inserido.
            if (offset + i) < t: # Se a posição mais o dado for menor que o tamanho do disco, ou seja, se os dado for ser escrito dentro do disco, para evitar que o dado seja escrito fora do disco. 
                paridade[offset + i] ^= dadosNovos[i] # Pega o valor atual da paridade e faz o xor com o byte do dado.

    abreParidade = open(discoParidade, 'wb') # Abre/cria o disco de paridade.
    abreParidade.write(paridade) # Escreve a paridade no disco de paridade.
    abreParidade.close() # Fecha o disco de paridade.

    print('- Disco de paridade discoX.bin atualizado com sucesso.') # Print para informa que o disco de paridade foi atualizado com sucesso.

def lerRAID(e, b, q, p): # Função que lê determinado conteúdo no disco de acordo com a posição indicada e a quantidade de bytes que deseja ler.
    # A lógica para encontrar o disco de acordo com a posição é a mesma feita na função escreveRAID.
    dadoDisco = e % (q-1) # O resto da divisão, da posição pela quantidade de discos, é em qual disco aquela posição está.

    offset = e // (q-1) # A divisão inteira, da posição pela quantidade de discos, para descobrir qual a posição em relação ao disco, ou seja, qual byte do disco representa aquela posição.
    
    caminho = os.path.join(p, f'disco{dadoDisco}.bin') # Pega o caminho que o disco desejado está.

    if os.path.exists(caminho): # Se o caminho existir.
        abreDisco = open(caminho, 'rb') # Abre o disco em formato de bytes.
        abreDisco.seek(offset) # Pula para a posição desejada.
        
        print(f'- {b} Bytes do disco{dadoDisco}.bin a partir da posição {offset}: {abreDisco.read(b)}') # Print do conteúdo de acordo com a quantidade de bytes informada.
        
        abreDisco.close() # Fecha o disco.    

    else: # Se o caminho não existir (caso o disco tenha sido removido).
        discos = os.listdir(p) # Uma lista dos discos que estão na pasta.

        nomeAusente = None # Para guardar o nome do disco ausente.

        bytesRecuperados = bytearray() # Para armazenar os bytes recuperados. 

        for i in range(q-1): # De acordo com a quantidade informada.
            if f'disco{i}.bin' not in discos: # Se o disco não estiver na lista da pasta de discos.
                nomeAusente = f'disco{i}.bin' # Pega o nome do disco que está ausente.       

        if f'discoX.bin' not in discos: # Se o disco de paridade não estiver na lista da pasta de discos.
            nomeAusente = 'discoX.bin' # Pega o nome do disco de paridade que está ausente.

        bytesRecuperados = bytearray() # Caso seja mais de um byte que deseja ser recuperado. 

        for posicao in range(offset, offset + b): # Percorre byte por byte.
            byteRecuperado = 0 # Cada byte do novo disco, vai ser um byte xor do discoX com outro disco, ou seja, um byte recuperado.

            for disco in discos: # Para cada disco na lista de discos.
                if disco != nomeAusente: # Se não for o novo disco criado.
                    caminho = os.path.join(p, disco) # Pega o caminho que o disco está, ou seja, pega o disco.
                        
                    abreDisco = open(caminho, 'rb') # Abre em formato de bytes.
                    abreDisco.seek(posicao) # Vai até na posição.
                        
                    byte = abreDisco.read(1) # Lê esse byte.

                    if byte: # Se foi possível a leitura.
                        byteRecuperado ^= byte[0] # Byte recuperado recebe o xor do byte.

                    abreDisco.close() # Fechamento do disco existente.

            bytesRecuperados.append(byteRecuperado) # Recebe cada byte recuperado.

        print(f'- {b} Bytes do disco{dadoDisco}.bin a partir da posição {offset}: {bytes(bytesRecuperados)}') # Print dos bytes recuperados.

def removeDiscoRAID(a, p): # Função que remove um determinado disco do RAID4.
    caminho = os.path.join(p, f'disco{a}.bin') # Pega o caminho que está o disco informado.

    if os.path.exists(caminho): # Se o disco informado existir no caminho.
        os.remove(caminho) # Remove o disco.

        print(f'- disco{a}.bin removido com sucesso.') # Print para informar que o disco foi removido com sucesso.

    else: # Se o disco informado não existir. 
        print('- Disco não encontrado.') # Print para informar que o disco não foi encontrado.

while True: # Enquanto for verdade.
    print('=== MENU RAID4 ===') # Menu de opções
    print('[1] - Inicializar RAID') # Opção 1 para inicializar o RAID.
    print('[2] - Obter RAID') # Opção 2 que obtem (verifica) o RAID.
    print('[3] - Reconstruir RAID') # Opção 3 que reconstroi um disco ausente no RAID.
    print('[4] - Escrever RAID') # Opção 4 que escreve um conjunto de dados em determinada posição no RAID.
    print('[5] - Ler RAID') # Opção 5 que lê um determinado número de bytes a partir de determinada posição no RAID.
    print('[6] - Remover RAID') # Opção 6 que remove determinado disco no RAID.
    print('[7] - Sair') # Opção 7 que finaliza o programa.

    opcao = int(input('Qual opção deseja? ')) # Pergunta de qual opção o usuário deseja.

    if opcao == 1: # Se a opção for 1.
        quantidadeDiscos = int(input('Quantos discos serão utilizados em RAID4? ')) # Pergunta quantos discos vão ser criados.
        tamanhoDiscos = int(input('Qual vai ser o tamanho dos discos em bytes? ')) # Pergunta qual vai ser o tamanho dos discos em bytes.
        pastaDiscos = str(input('Em qual pasta os discos devem ser criados? ')) # Pergunta onde os discos devem ser criados.

        inicializaRAID(quantidadeDiscos, tamanhoDiscos, pastaDiscos) # Chamada da função para criar os discos e armazena-los.

    elif opcao == 2: # Se a opção for 2.
        obtemRAID(quantidadeDiscos, pastaDiscos) # Chamada da função que verifica os discos criados.

    elif opcao == 3: # Se a opção for 3.
        reconstroiRAID(quantidadeDiscos, tamanhoDiscos, pastaDiscos) # Chamada da função que reconstroi um disco faltante.

    elif opcao == 4: # Se a opção for 4.
        conjuntoDados = str(input('Qual conjunto de dados inserir no RAID? ')) # Pergunta qual conjunto de dados o usuário quer inserir.
        posicao = int(input('Em qual posição deseja inserir? ')) # Pergunta em qual posição ele quer inserir o conjunto de dados.
        escreveRAID(conjuntoDados, posicao, quantidadeDiscos, pastaDiscos, tamanhoDiscos) # Chamada da função para inserir um conjunto de dados em um posição.

    elif opcao == 5: # Se a opção for 5.
        existePosicao = int(input('Qual posição deseja ler? ')) # Pergunta qual posição o usuário deseja ler.
        quantBytes = int(input('Quantos bytes deseja ler? ')) # Pergunta quantos bytes a partir daquela posição o usuário deseja ler.
        lerRAID(existePosicao, quantBytes, quantidadeDiscos, pastaDiscos) # Chamada da função para ler determinada quantidade de bytes em determinada posição.

    elif opcao == 6: # Se a opção for 6.
        apagarDisco = int(input('Informe qual disco deseja remover? ')) # Chamada da função para remover determinado disco do RAID4.

        removeDiscoRAID(apagarDisco, pastaDiscos) # Chamada da função que remove o disco indicado. 

    elif opcao == 7: # Se a opção for 7.
        print('=== Programa encerrado ===') # Print do encerramento do programa.
        break # O programa para.

    else: # Se não for nenhuma das opções acima.
        print('--- Opção inválida. ---') # Print de que a opção é inválida e o menu aparece novamente.
'''

'''
## RAID5

import os

def inicializaRAID(q, t, p): # Função que cria e armazena os discos. 
    for i in range(q): # De acordo com a quantidade de discos informados.
        caminho = os.path.join(p, f'disco{i}.bin') # Pega o caminho que está a pasta para criar o disco.
        
        disco = open(caminho, 'wb+') # Abre/cria o disco em formato de bytes.
        
        disco.write(b'\x00' * t) # Escreve no disco de acordo com o tamanho informado.

        disco.close() # Fecha o disco.

        print(f'- disco{i}.bin criado com sucesso.') # Print do disco que foi criado com sucesso.
  
def obtemRAID(q, p): # Função para verificar os discos criados.
    discos = os.listdir(p) # Uma lista dos discos que estão na pasta.
    
    ausentes = 0 # Para contar quantos discos estão ausentes.

    for i in range(q): # De acordo com a quantidade informada.
        if f'disco{i}.bin' in discos: # Se o disco estiver na lista da pasta de discos.
            print(f'- disco{i}.bin presente.') # Print do disco que está presente.
        
        else: # Se o disco estiver ausente.
            print(f'- disco{i}.bin ausente.') # Print do disco que está ausente, ou seja, que deveria ter sido criado.
            
            ausentes += 1 # Se o disco estiver ausente, o contador recebe mais um.

    if ausentes >= 2: # Se tiver mais de um disco ausente, o RAID será inválido.
        print('Mais de um disco ausente!\n --- RAID inválido ---') # Print do RAID inválido.
        return # O programa não deve continuar.

    else: # Se não, o RAID será válido.
        print('--- RAID válido ---') # Print do RAID válido.

def reconstroiRAID(q, t, p): # Função para construir um disco ausente.
    discos = os.listdir(p) # Uma lista dos discos que estão na pasta.

    nomeAusente = None # Para guardar o nome do disco ausente.

    for i in range(q): # De acordo com a quantidade informada.
        if f'disco{i}.bin' not in discos: # Se o disco não estiver na lista da pasta de discos.
            nomeAusente = f'disco{i}.bin' # Pega o nome do disco que está ausente.       

    if nomeAusente is not None: # Se o nomeAusente não estiver vazio, ou seja, tem um disco ausente, ele vai reconstruir o disco.
        caminhoAusente = os.path.join(p, nomeAusente) # Caminho do disco ausente.
        novoDisco= open(caminhoAusente, 'wb') # Abre/cria o novo disco, ou seja, o disco que estava ausente.

        for linha in range(t): # Para cada byte do tamanho.
            xor = 0 # Para armazenar o xor (o byte) que será recuperado.

            for disco in discos: # Para cada disco na lista de discos.
                if disco != nomeAusente: # Se não for o novo disco criado.
                    caminho = os.path.join(p, disco) # Pega o caminho que o disco está, ou seja, pega o disco.
                    
                    abreDisco = open(caminho, 'rb') # Abre em formato de bytes.
                    abreDisco.seek(linha) # Vai até a posição da linha.
                    
                    byte = abreDisco.read(1) # Lê esse byte.

                    if byte: # Se foi possível a leitura.
                        xor ^= byte[0] # Faz o xor para recuperar o byte perdido.

                    abreDisco.close() # Fechamento do disco.

            novoDisco.write(bytes([xor])) # Escreve o byte recuperado no novo disco.

        novoDisco.close() # Ao final, fecha o novo disco.

        print(f'{nomeAusente} reconstruído com sucesso.')

def escreveRAID(c, p, q, pd): # Função que escreve um conjunto de dados em determinado disco.
    linha = p // (q-1) # Como no RAID5 os disco são compartilhados, é como imaginar que todos os discos formam uma tabela, assim se deve descobrir a linha, ou seja, em qual linha do RAID o dado será gravado.

    coluna = p % (q-1) # Descobre qual a coluna daquela linha, para achar exatamente a posição lógica do dado que será armazenado.

    paridade = linha % q # Descobre a posição armazena a paridade naquela linha.

    if coluna >= paridade: # Se a coluna for maior ou igual a paridade, ou seja, se o dado que será armazenado estiver na mesma posição que a paridade, ou maior porque no RAID5 precisamos pular o disco que está armazenando a paridade naquela linha.
        disco = coluna + 1 # Pula o disco de paridade para encontrar o disco real do dado.

    else: # Se não
        disco = coluna # O disco é igual a coluna, ou seja, é a posição onde o dado será armazenado.

    caminho = os.path.join(pd, f'disco{disco}.bin') # Pega o caminho que o disco está.

    dados = c.encode("utf-8") # Transforma o conjunto de dados em bytes.

    for i in range(len(dados)): # Em cada byte que está em dados.
        posicaoAtual = p + i # Para descobrir a posição lógica de cada byte.

        linha = posicaoAtual // (q-1) # Pega a linha, ou seja, em qual linha do RAID o dado será gravado.

        coluna = posicaoAtual % (q-1) # Descobre qual a coluna daquela linha, para achar exatamente a posição lógica do dado que será armazenado.

        paridade = linha % q # Descobre a posição armazena a paridade naquela linha.

        if coluna >= paridade: # Se a coluna for maior ou igual a paridade, ou seja, se o dado que será armazenado estiver na mesma posição que a paridade, ou maior porque no RAID5 precisamos pular o disco que está armazenando a paridade naquela linha.
            disco = coluna + 1 # Pula o disco de paridade para encontrar o disco real do dado.

        else: # Se não
            disco = coluna # O disco é igual a coluna, ou seja, é a posição onde o dado será armazenado.

        caminho = os.path.join(pd, f'disco{disco}.bin') # Pega o caminho que o disco está.

        if os.path.exists(caminho): # Se o caminho existir.
            abreDisco = open(caminho, 'rb+') # Abre o disco em formato de bytes.
            abreDisco.seek(linha) # Pula para a posição da linha.
            abreDisco.write(bytes([dados[i]])) # Escreve o byte, em bytes, na posição.
            abreDisco.close() # Fecha o disco.

            print(f'- Dados inseridos em disco{disco}.bin com sucesso.') # Print para informar que os dados foram inseridos no disco certo de acordo com a posição informada.

        else: # Se o caminho não existir.
            print(f'- disco{disco}.bin está ausente.') # Print para informar que o disco está ausente.
            print('- Os dados não foram escritos diretamente no disco.') # Print para informar que os dados não foram gravados diretamente no disco.

        xor = dados[i] # O xor tem que ser igual o byte novo que será gravado.

        for discoAtual in range(q): # Enquanto na quantidade de discos.
            if discoAtual != paridade and discoAtual != disco: # Se não for o disco que armazena a paridade daquela linha e o disco atual for diferente do disco, ou seja, se não for o ausente.
                caminhoDisco = os.path.join(pd, f'disco{discoAtual}.bin') # Pega o caminho que o disco está.
                
                if os.path.exists(caminhoDisco): # Se o caminho existe.
                    abreDisco = open(caminhoDisco, 'rb') # Abre o disco em formato de bytes.
                    abreDisco.seek(linha) # Pula para a posição da linha.
                
                    byte = abreDisco.read(1) # Lê o byte daquela linha.

                    if byte: # Se foi possível a leitura.
                        xor ^= byte[0] # Cálculo da paridade, um xor daquele byte. 

                    abreDisco.close() # Fecha o disco.

        caminhoParidade = os.path.join(pd, f'disco{paridade}.bin') # Caminho do disco que vai receber a paridade atualizada.
    
        abreParidade = open(caminhoParidade, 'rb+') # Abre o disco como bytes.
        abreParidade.seek(linha) # Pula para a posição da linha.
        abreParidade.write(bytes([xor])) # Escreve o byte da paridade calculada.
        abreParidade.close() # Fecha o disco.

        print('- Paridade atualizada com sucesso.') # Print para informa que a paridade foi atualizado com sucesso.

def lerRAID(e, b, q, p): # Função que lê determinado conteúdo no disco de acordo com a posição indicada e a quantidade de bytes que deseja ler.
    bytesLidos = bytearray() # Para armazenar os bytes lidos.
    
    for i in range(b): # Enquanto em cada byte desejado.
        posicaoAtual = e + i # Para descobrir a posição lógica de cada byte.

        linha = posicaoAtual // (q-1) # Pega a linha, ou seja, em qual linha do RAID o dado será lido.

        coluna = posicaoAtual % (q-1) # Descobre qual a coluna daquela linha, para achar exatamente a posição lógica do dado que será lido.

        paridade = linha % q # Descobre a posição armazena a paridade naquela linha.

        if coluna >= paridade: # Se a coluna for maior ou igual a paridade, ou seja, se o dado que será armazenado estiver na mesma posição que a paridade, ou maior porque no RAID5 precisamos pular o disco que está armazenando a paridade naquela linha.
            disco = coluna + 1 # Pula o disco de paridade para encontrar o disco real do dado.

        else: # Se não
            disco = coluna # O disco é igual a coluna, ou seja, é a posição onde o dado será armazenado.

        caminho = os.path.join(p, f'disco{disco}.bin') # Pega o caminho que o disco está.

        if os.path.exists(caminho): # Se o caminho existir.
            abreDisco = open(caminho, 'rb') # Abre o disco em formato de bytes.
            abreDisco.seek(linha) # Pula para a posição desejada.

            byte = abreDisco.read(1) # Lê o byte daquela linha.

            if byte: # Se foi possível a leitura.       
                bytesLidos.append(byte[0]) # Recebe cada byte lido.

            abreDisco.close() # Fecha o disco.

            print(f'- {b} Bytes do disco{disco}.bin a partir da posição {linha}: {bytes(bytesLidos)}') # Print do conteúdo de acordo com a quantidade de bytes informada.        

        else: # Se o caminho não existir (caso o disco tenha sido removido).
            print(f'- disco{disco}.bin está ausente.') # Print para informar que o disco está ausente.
            print('- Os dados foram recuperados usando XOR.') # Print para informar que os dados foram recuperados usando XOR (paridade).

            xor = 0 # Para armazenar o xor (paridade) que será calculada.

            for discoAtual in range(q): # Enquanto na quantidade de discos.
                if discoAtual != disco: # Se o disco atual for diferente do disco, ou seja, se não for o ausente.
                    caminhoDisco = os.path.join(p, f'disco{discoAtual}.bin') # Pega o caminho que o disco está.
                    
                    if os.path.exists(caminhoDisco): # Se o caminho existe.
                        abreDisco = open(caminhoDisco, 'rb') # Abre o disco em formato de bytes.
                        abreDisco.seek(linha) # Pula para a posição da linha.
                    
                        byte = abreDisco.read(1) # Lê o byte daquela linha.

                        if byte: # Se foi possível a leitura.
                            xor ^= byte[0] # Cálculo da paridade, um xor daquele byte. 

                        abreDisco.close() # Fecha o disco.

            bytesLidos.append(xor) # Recebe cada byte recuperado lido.

            print(f'- {b} Bytes recuperados do disco{disco}.bin ausente a partir da posição {linha}: {bytes(bytesLidos)}') # Print dos bytes recuperados do disco ausente de acordo com a quantidade de bytes informada e a posição.

def removeDiscoRAID(a, p): # Função que remove um determinado disco do RAID5.
    caminho = os.path.join(p, f'disco{a}.bin') # Pega o caminho que está o disco informado.

    if os.path.exists(caminho): # Se o disco informado existir no caminho.
        os.remove(caminho) # Remove o disco.

        print(f'- disco{a}.bin removido com sucesso.') # Print para informar que o disco foi removido com sucesso.

    else: # Se o disco informado não existir. 
        print('- Disco não encontrado.') # Print para informar que o disco não foi encontrado.

while True: # Enquanto for verdade.
    print('=== MENU RAID5 ===') # Menu de opções
    print('[1] - Inicializar RAID') # Opção 1 para inicializar o RAID.
    print('[2] - Obter RAID') # Opção 2 que obtem (verifica) o RAID.
    print('[3] - Reconstruir RAID') # Opção 3 que reconstroi um disco ausente no RAID.
    print('[4] - Escrever RAID') # Opção 4 que escreve um conjunto de dados em determinada posição no RAID.
    print('[5] - Ler RAID') # Opção 5 que lê um determinado número de bytes a partir de determinada posição no RAID.
    print('[6] - Remover RAID') # Opção 6 que remove determinado disco no RAID.
    print('[7] - Sair') # Opção 7 que finaliza o programa.
    
    opcao = int(input('Qual opção deseja? ')) # Pergunta de qual opção o usuário deseja.
    
    if opcao == 1: # Se a opção for 1.
            quantidadeDiscos = int(input('Quantos discos serão utilizados em RAID5? ')) # Pergunta quantos discos vão ser criados em RAID5.
            tamanhoDiscos = int(input('Qual vai ser o tamanho dos discos em bytes? ')) # Pergunta qual vai ser o tamanho dos discos em bytes.
            pastaDiscos = str(input('Em qual pasta os discos devem ser criados? ')) # Pergunta onde os discos devem ser criados.

            inicializaRAID(quantidadeDiscos, tamanhoDiscos, pastaDiscos) # Chamada da função para criar os discos e armazena-los na pasta informada.

    elif opcao == 2: # Se a opção for 2.
        obtemRAID(quantidadeDiscos, pastaDiscos) # Chamada da função que verifica os discos criados.

    elif opcao == 3: # Se a opção for 3.
        reconstroiRAID(quantidadeDiscos, tamanhoDiscos, pastaDiscos) # Chamada da função que reconstroi um disco faltante.

    elif opcao == 4: # Se a opção for 4.
        conjuntoDados = str(input('Qual conjunto de dados inserir no RAID? ')) # Pergunta qual conjunto de dados o usuário quer inserir.
        posicao = int(input('Em qual posição deseja inserir? ')) # Pergunta em qual posição ele quer inserir o conjunto de dados, ou seja, em qual disco.
        escreveRAID(conjuntoDados, posicao, quantidadeDiscos, pastaDiscos) # Chamada da função para inserir um conjunto de dados em um posição.

    elif opcao == 5: # Se a opção for 5.
        existePosicao = int(input('Qual posição deseja ler? ')) # Pergunta qual posição o usuário deseja ler.
        quantBytes = int(input('Quantos bytes deseja ler? ')) # Pergunta quantos bytes a partir daquela posição o usuário deseja ler.
        lerRAID(existePosicao, quantBytes, quantidadeDiscos, pastaDiscos) # Chamada da função para ler determinada quantidade de bytes em determinada posição.
        
    elif opcao == 6: # Se a opção for 6.
        apagarDisco = int(input('Informe qual disco deseja remover: ')) # Chamada da função para remover determinado disco do RAID5.
        removeDiscoRAID(apagarDisco, pastaDiscos) # Chamada da função que remove o disco indicado.

    elif opcao == 7: # Se a opção for 7.
        print('=== Programa encerrado ===') # Print do encerramento do programa.
        break # O programa para.

    else: # Se não for nenhuma das opções acima.
        print('--- Opção inválida. ---') # Print de que a opção é inválida e o menu aparece novamente.
                    
'''