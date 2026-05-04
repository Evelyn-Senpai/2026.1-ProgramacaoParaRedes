'''
Os 24 bytes do cabeçalho global (PCAP)

[0-3]   → Magic Number
[4-5]   → Version Major
[6-7]   → Version Minor
[8-11]  → This Zone (GMT offset)
[12-15] → Sigfigs (precisão do timestamp)
[16-19] → SnapLen (tamanho máximo capturado)
[20-23] → Network (tipo de enlace)

Cabeçalho do pacote (16 bytes)

[0-3]   → Timestamp (segundos)
[4-7]   → Timestamp (microsegundos)
[8-11]  → incl_len (tamanho capturado)
[12-15] → orig_len (tamanho original)

'''