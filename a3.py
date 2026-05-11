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
import os

def inicializaRAID(q, t, p): # Função que cria e armazena os discos. 
    for i in range(0, q-1): # De acordo com a quantidade de discos informados, menos um, porque o último disco tem que ser o de paridade.
        caminho = os.path.join(p, f'disco{i}.bin') # Pega o caminho que está a pasta para criar o disco.
        
        disco = open(caminho, 'wb+') # Abre/cria o disco em formato de bytes.
        disco.write(b'\x00' * t) # Escreve no disco de acordo com o tamanho informado.
        disco.close() # Fecha o disco.
    
    discoParidade = os.path.join(p, f'discoX.bin') # Cria o disco de paridade.
    paridade = bytearray(t) # Um array vazio com o tamanho que foi informado para os discos que foram digitados.

    discos = os.listdir(p) # Uma lista dos discos que estão na pasta.
    for disco in discos: # Em cada nome do disco.
        if disco != 'discoX.bin': # Se o disco não for o de paridade, porque o disco de paridade não entra no cálculo da própria paridade.
            caminho = os.path.join(p, disco) # Pega o caminho que o disco está, ou seja, pega o disco.

            abreDisco = open(caminho, 'rb') # Abre/cria em formatado de bytes.        
            dados = abreDisco.read() # Lê o conteúdo do disco.

            for i in range(len(dados)): # Em cada byte que está em dados.
                paridade[i] ^= dados[i] # Em cada posição no array de bytes, recebe um xor dos dados de cada disco naquela posição. 

    abreParidade = open(discoParidade, 'wb') # Abre/cria o disco de paridade.
    abreParidade.write(paridade) # Escreve a paridade no disco de paridade.
    abreParidade.close() # Fecha o disco de paridade.

def obtemRAID(q, p): # Função para verificar os discos criados.
    discos = os.listdir(p) # Uma lista dos discos que estão na pasta.
    
    ausentes = 0 # Para contar quantos discos estão ausentes.

    for i in range(q-1): # De acordo com a quantidade informada.
        if f'disco{i}.bin' in discos: # Se o disco estiver na lista da pasta de discos.
            print(f'disco{i}.bin criado com sucesso.') # Print do disco que foi criado com sucesso.
        
        else: # Se o disco estiver ausente.
            print(f'disco{i}.bin ausente.') # Print do disco que está ausente, ou seja, que deveria ter sido criado.
            
            ausentes += 1 # Se o disco estiver ausente, o contador recebe mais um.

    if f'discoX.bin' in discos: # Se o disco de paridade estiver na lista da pasta de discos.
        print(f'discoX.bin criado com sucesso.') # Print do disco de paridade que foi criado com sucesso.
        
    else: # Se o disco de paridade estiver ausente.
        print(f'discoX.bin ausente.') # Print do disco de paridade que está ausente.
            
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
                    
                    abreDisco = open(caminho, 'rb') # Abre em formatado de bytes.
                    abreDisco.seek(i) # Vai até a posição i, e em posição em posição.
                    
                    byte = abreDisco.read(1) # Lê esse byte.
                    byteRecuperado ^= byte[0] # Byte recuperado recebe o xor do byte.

                    abreDisco.close() # Fechamento do disco existente.

            novoDisco.write(bytes([byteRecuperado])) # Escreve o byte recuperado no novo disco.

        novoDisco.close() # Ao final, fecha o novo disco.

        print(f'{nomeAusente} reconstruído com sucesso.')

quantidadeDiscos = int(input('Quantos discos serão utilizados em RAID4? ')) # Pergunta quantos discos vão ser criados.
tamanhoDiscos = int(input('Qual vai ser o tamanho dos discos em bytes? ')) # Pergunta qual vai ser o tamanho dos discos em bytes.
pastaDiscos = str(input('Em qual pasta os discos devem ser criados? ')) # Pergunta de onde os discos devem ser criados.
print('-------------------------------------------------------')
inicializaRAID(quantidadeDiscos, tamanhoDiscos, pastaDiscos) # Chamada da função para criar os discos e armazena-los.
obtemRAID(quantidadeDiscos, pastaDiscos) # Chamada da função que verifica os discos criados.
reconstroiRAID(quantidadeDiscos, tamanhoDiscos, pastaDiscos) # Chamada da função que reconstroi um disco faltante.