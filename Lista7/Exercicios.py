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

#Questão 14
def ex14():
    salario = float(input('Insira seu salário: '))
    if (salario<=600):
        print('Isento de desconto')
    elif (salario>600) and (salario<=1200):
        print('Esse é o desconto: ', salario*0.2)
    elif(salario>1200) and (salario<=2000):
        print('Esse é o desconto: ', salario*0.25)
    else: 
        print('Esse é o desconto: ', salario*0.3)

#Questão 15
def ex15():
    preco = float(input('Coloque o preço do produto: '))
    codigo = int(input('Coloque o código do produto: '))
    if (codigo==1):
        print('O preço final é ', preco, 'na região Sudeste')
    elif (codigo==2):
        print('O preço final é ', preco, 'na região Sul')
    elif (codigo==3):
        print('O preço final é ', preco, 'na região Cnetro-Oeste')
    elif (codigo==4):
        print('O preço final é ', preco, 'na região Nordeste')
    elif (codigo==5):
        print('O preço final é ', preco, 'na região Norte')
    else:
        print('O produto é importado e seu preço final é ', preco*1.15)

#Questão 16
def ex16():
    a = int(input('Insira um número: '))
    b = int(input('Insira um número: '))
    c = int(input('Insira um número: '))
# Vou precisar ver só 3 situações: se o 1 é maior que o 2; se o 2 é maior que o 3; se o 3 é maior que o 2
    if (a<b): 
        temp = a
        a = b 
        b = temp
    if (a<c):
        temp = a
        a = c
        c = temp
    if(b<c):
        temp = b
        b = c
        c = temp
    print(a,b,c)

#Questão extra
def ex17():
    a = int(input('Insira um número: '))
    b = int(input('Insira um número: '))
    c = int(input('Insira um número: '))
    d = int(input('Insira um número: '))
    if (a>b):
        temp = a
        a = b
        b = temp
    if (a>c):
        temp = a
        a = c
        c = temp
    if (a>d):
        temp = a
        a = d
        d = temp
    if (b>c):
        temp = b
        b = c
        c = temp 
    if (b>d):
        temp = b
        b = d
        d = temp
    if (c>d):
        temp = c
        c = d
        d = temp
    print('A ordem crescente é: ', a , b , c , d)
#Lembre-se de que todo mundo deve receber algo, você estava trocando e alguns ficaram sem valor