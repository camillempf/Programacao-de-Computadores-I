#Questão 1: Crie um intervalo, utilizando range, de 0 a 50, excluindo 50.
def ex1():
    intervalo = range(0,50)
    print(list(intervalo))

#Questão 2: Crie um intervalo, utilizando range, de 0 a 10, incluindo o 10 com passos de 2 em 2.
def ex2(): 
    intervalo = range (0,11,2)
    print(list(intervalo))

#Questão 3: Crie um intervalo [10, 4), utilizando range, com passos de -1 em -1.
def ex3(): 
    intervalo = range(10,4,-1)
    print(list(intervalo))

#Questão 4: Crie um intervalo [67,54), utilizando range, com passos de -2 em -2.
def ex4():
    conjunto = range(67,54,-2)
    print(list(conjunto))


#Questão 8: Escrever um programa que leia 5 valores, um de cada vez, e conta quantos deles estão em cada um dos intervalos: [0, 25], (25, 50], (50, ∞).
def ex8():
    for k in range (0,5,1):
        k = int(input('Coloque um número: '))
        if (k>=0) and (k<=25):
            print('Esse número está no intervalo entre 0 e 25')
        elif (k>25) and (k<=50): 
               print('Esse número está no intervalo entre 25 e 50')
        else:
               print('Esse número é maior que 50')

#Questão 9: Escreva um programa que leia 5 valores inteiros, um de cada vez e calcule a soma deles.
def ex9():
    soma = 0
    for i in range (5):
        valor = int(input('Insira um número: '))
        soma = soma + valor 
    print('A soma desses números é: ', soma)
    
#Questão 10: Escreva um programa que leia 5 valores inteiros, um de cada vez, e calcule a média aritmética dos números lidos.
def ex10():
    soma = 0 
    for i in range (5):
        n = int(input('Insira um número: '))
        soma = soma + n
    media = soma / 5
    print('Essa é a média: ', media)

#Questão 11: Escreva um programa que leia 5 valores inteiros, um de cada vez. Encontrar e escrever o maior valor lido.
def ex11(): 
    maior = int(input('Insira um número: '))
    for i in range (4):
        valor = int(input('Insira um número: '))
        if valor > maior: 
            maior = valor
    print('Esse é o maior número: ', maior)

