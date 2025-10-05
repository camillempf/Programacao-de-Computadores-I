ano = int(input('Selecione o ano: '))
if (ano%4==0) or (400%ano==0) and (ano!=1800) and (ano!=1900) and (ano!=2000):
    print('Esse ano é bissexto: ', ano)
else: 
    print('Esse ano não é bissexto: ', ano)
