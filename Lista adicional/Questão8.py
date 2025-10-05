import math
for g in range (0,55,3):
    a = float(input('Qual o tamanho do lado do triângulo?'))
    b = float(input('Qual o tamanho do lado do triângulo?'))
    c = float(input('Qual o tamanho do lado do triângulo?'))
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print('Essa é a área do triângulo: ', area)
