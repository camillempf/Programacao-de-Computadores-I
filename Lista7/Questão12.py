maior = 0
for i in range (0,5,2):
    a = int(input('Qual sua altura? '))
    m = int(input('Qual sua matrícula? '))
if a > maior: 
    temp = a
    a = maior
    maior = temp
print('essa é a maior altura: ', a, 'e sua matrícula é: ', m)
