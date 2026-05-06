'''
Os 24 bytes do cabeçalho global (PCAP)
'''
# [0-3]   → Magic Number
# [4-5]   → Version Major
# [6-7]   → Version Minor
# [8-11]  → This Zone (GMT offset)
# [12-15] → Sigfigs (precisão do timestamp)
# [16-19] → SnapLen (tamanho máximo capturado)
# [20-23] → Network (tipo de enlace)
'''
Cabeçalho do pacote (16 bytes)
'''
# [0-3]   → Timestamp (segundos)
# [4-7]   → Timestamp (microsegundos)
# [8-12]  → incl_len (tamanho capturado)
# [12-16] → orig_len (tamanho original)
'''
Estrutura do quadro Ethernet (14 bytes) [Cabeçalho Ethernet] + [Dados]
'''
# [0-5]   → MAC destino
# [6-11]  → MAC origem
# [12-13] → Tipo (0x0800 = IPv4; 0x0806 = ARP)
'''
Estrutura do pacote IPv4 (20 bytes (no mínimo)) [Cabeçalho IPv4] + [Dados]
'''
# [0]   Versão + IHL
# [1]   Tipo de serviço (DSCP/ECN)
# [2-3] Tamanho total
# [4-5] Identificação
# [6-7] Flags + Fragment Offset
# [8]   TTL
# [9]   Protocolo
# [10-11] Checksum do cabeçalho
# [12-15] IP de origem
# [16-19] IP de destino
# [20+] Opções (se houver)
# (Se não)
# [23] Protocolo (6 = TCP, 17 = UDP) → offset variável (depende do IHL(IHL × 4 = tamanho do cabeçalho))
# [26-29] → IP origem
# [30-33] → IP destino
'''
Estrutura do pacote ARP (28 bytes) [Cabeçalho ARP] + [Dados]
'''
# [0-1]   → Hardware Type (HTYPE)
# [2-3]   → Protocol Type (PTYPE)
# [4]     → Hardware Size (HLEN)
# [5]     → Protocol Size (PLEN)
# [6-7]   → Operation (Opcode)
# [8-13]  → Sender MAC Address
# [14-17] → Sender IP Address
# [18-23] → Target MAC Address
# [24-27] → Target IP Address
'''
Estrutura de segmento TCP (20 bytes (no mínimo)) [Cabeçalho TCP] + [Dados]
'''
# [0-1]   → Porta de origem
# [2-3]   → Porta de destino
# [4-7]   → Número de sequência
# [8-11]  → Número de confirmação (ACK)
# [12] → Data Offset (4 bits) + Reserved (Data Offset × 4 = tamanho do cabeçalho)
# [13] → Flags (Controlam conexão (SYN, ACK, FIN, etc.))
# [14-15] → Janela (Window Size)
# [16-17] → Checksum
# [18-19] → Ponteiro urgente
# [20+]   → Opções (se existirem)
'''
Estrutura de segmento UDP (8 Bytes) [Cabeçalho UDP] + [Dados]
'''
# [0-1] → Porta de origem
# [2-3] → Porta de destino
# [4-5] → Comprimento (Length)
# [6-7] → Checksum