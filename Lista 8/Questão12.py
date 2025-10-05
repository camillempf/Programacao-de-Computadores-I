maiormat = 0
menormat = 0
maior = 0 
menor = 10
mat = int(input('Qual sua matrícula? '))
alt = float(input('Qual sua altura? '))
for g in range (0,10,2):
    mat = int(input('Qual sua matrícula? '))
    alt = float(input('Qual sua altura? '))
    if alt > maior: 
       maior = alt
       maiormat = mat
    if alt < menor:
        menor = alt
        menormat = mat
print('O aluno com matrícula ', maiormat, 'tem a maior altura, a qual é ', maior)
print('O aluno com matrícula ', menormat, 'tem a menor altura, a qual é ', menor)