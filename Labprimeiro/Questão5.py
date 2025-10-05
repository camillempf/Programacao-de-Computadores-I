nome = input('Qual o seu nome? ')
n1 = float(input('Insira sua nota1: '))
n2 = float(input('Insira sua nota2: '))
n3 = float(input('Insira sua nota3: '))
n4 = float(input('Insira sua nota4: '))
media = (n1+n2+n3+n4)/4
if media >= 7:
    print('Nome: ', nome, 'sua média é: ', media, '- aprovado')
else:
    print('Nome: ', nome, 'sua média é: ', media, 'reprovado')
    