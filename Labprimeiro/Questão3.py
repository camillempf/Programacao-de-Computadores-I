n = int(input('Insira um número: '))
if n%2==0 and n>0:
    print('Esse número é par e positivo')
if n%2==0 and n<0:
    print('Esse número é par e negativo')
elif n%2!=0 and n>0:
    print('Esse número é ímpar e positivo')
elif n%2!=0 and n<0:
    print('Esse número é ímpar e negativo')