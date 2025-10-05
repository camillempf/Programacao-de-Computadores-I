for m in range (15):
    t = float(input('Qual a taxa?'))
    p = float(input('Qual a prestação?'))
    atraso = p + (p*t/100)
    print('Esse é o juros pelo atraso: ', atraso)
    