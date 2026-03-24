'''
Diremos que um número de n dígitos é pandigital se ele utiliza todos os dígitos de 1 
até n exatamente uma vez. 
Por exemplo, 2143 é um número pandigital de 4 dígitos e também é primo. 
Qual é o maior número primo pandigital de n dígitos que existe?
'''

def primo(n):
    tot = 0
    for c in range(1, n+1):
        if n % c == 0:
            tot += 1
    if tot == 2:
        return True
    else:
        return False
def pandigital(n):
    return sorted(str(n)) == [str(i) for i in range(1, len(str(n))+1)]

maior = 0    
for i in range(1, 10000):
    if primo(i) and pandigital(i):
        if i == 1:
            maior = menor = i
        else:
            if i > maior:
                maior = i 
print('Esse é o maior número primo pandigital: ', maior)
