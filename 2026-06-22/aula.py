'''Programação com Threads'''

import threading, time

# --- Ex1 Threads ---
NVOLTAS = 5
def carro_f1(nome_piloto, velocidade):
    global vencedor
    # print(f'{nome_piloto} largou...')
    # lck.acquire()
    voltas = 0
    while voltas < NVOLTAS:
        time.sleep(1/velocidade)
      
        lck.acquire()

        voltas += 1
        
        if voltas == NVOLTAS and vencedor == None:
            vencedor = nome_piloto

        lck.release()

        print(f'{nome_piloto}: {time.ctime(time.time())} ... {voltas}')

    # lck.acquire()

    print(f'{nome_piloto} concluiu a prova!')

    # if vencedor == None:
    #     vencedor = nome_piloto

    # lck.release()

# def meuprint(msg):
#     print(msg)

try:
    vencedor = None
    pilotos = []
    lck = threading.Lock()

    piloto1 = threading.Thread(target=carro_f1, args=('Lewis Hamilton', 2.002))
    piloto2 = threading.Thread(target=carro_f1, args=('Sebastian Vettel', 2.001))
    piloto3 = threading.Thread(target=carro_f1, args=('Max Verstappen', 2.003))

    piloto1.start()
    piloto2.start()
    piloto3.start()

    piloto1.join()
    piloto2.join()
    piloto3.join()

    print('A corrida acabou!!')

    print(f'O vencedor foi {vencedor}!!!')

except:
    print('ERRO: Não foi possível iniciar a corrida.')
