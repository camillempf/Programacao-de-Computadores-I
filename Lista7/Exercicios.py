import math

#Questão 1
def ex1():
    a = int(input('Escreva um  número '))
    b = int(input('Escreva outro número '))
    if (a==b):
        print('São iguais')
    else: 
        print('São diferentes')

#Questão 2
def ex2():
    a = int(input('Insira um número: '))
    b = int(input('Insira outro número: '))
    if (a%b==0) or (b%a==0):
        print('São múltiplos')
    else: 
        print('Não são múltiplos')

#Questão 3
def ex3():
    a = int(input('Insira um número: '))
    if (a%3==0) and (a%7==0):
        print('Esse número é múltiplo de 3 e de 7 simultaneamente')
    else: 
        print('Não é múltplo simultâneo de 3 e de 7')

#Questão 4
def ex4():
    h = float(input('Insira sua altura: '))
    b = input('Seu sexo é masculino ou feminino? ')
    if (b=="masculino"):
        calculo = (72.7 * h) - 58
        print('Seu peso ideal é: ', calculo)
    else:
        calculo = (62.1 * h) - 44.7
        print ('Seu peso ideal é: ', calculo)

#Questão 5
def ex5():
    a = int(input('Qual a sua idade? '))
    if (a<18):
        print('Você é menor de idade')
    elif (a>= 18) and (a<=65):
        print('Você é maior de idade')
    else:
        print('Você tem mais que 65 anos de idade')

#Questão 6
def ex6():
    a = int(input('Insira um número: '))
    if (a>0) and (a<10) and (a%2==0):
        print('Esse número é par e menor que 10')
    elif (a>0) and (a<10) and (a%2!=0):
        print('Esse número é ímpar e menor que 10')
    else: 
        print('Esse número não está no intervalo')

#Questão 7 
def ex7():
    a = int(input('Escreva um número: '))
    if (a==5):
        print('é igual a 5')
    elif (a==200):
        print('é igual a 200')
    elif (a==400):
        print('é igual a 400')
    elif (a>=500) and (a<=1000):
        print('está no intervalo entre 500 e 1000')
    else:
        print('está fora dos intervalos anteriores')

#Questão 8
def ex8():
    a = int(input('Insira um número: '))
    if (a>=0):
        calculo = math.sqrt(a)
        print('a raiz quadrada de', a , 'é', calculo)
    else:
        continha = (a**2)
        print('o quadrado de', a , 'é', continha)

#Questão 9 
def ex9():
    nota1 = float(input('insira sua nota: '))
    nota2 = float(input('insira sua outra nota: '))
    media = (nota1 + nota2)/2
    if (media>=7):
        print('aprovado com a média', media)
    elif (media<7) and (media>=3):
        print('exame com a média', media)
    else:
        print('reprovado com a média', media)

#Questão 10 
def ex10():
    a = float(input('insira um número'))
    b = float(input('insira um número'))
    c = float(input('insira um número'))
    if (a>b) and (a>c):
        print(a, 'é o maior número')
    elif (b>a) and (b>c):
        print(b, 'é o maior número')
    else:
        print(c, 'é o maior número')

#Questão 11
def ex11():
    a = float(input('insira um número'))
    b = float(input('insira um número'))
    c = float(input('insira um número'))
    if (a<b) and (a<c):
        print(a, 'é o menor número')
    elif (b<a) and (b<c):
        print(b, 'é o menor número')
    else:
        print(c, 'é o menor número')

    