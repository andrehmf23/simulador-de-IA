#x:3 d:2 W:2 B:1 Y:temporario ERRO:temporario

def functionSave():
    while i != linhas:
        print(i)
        print(linhas)
        x1 = x1 + [int(input("x1 []: "))]
        x2 = x2 + [int(input("x2 []: "))]#<-limitado só x1 e x2
        d = d + [int(input("d []: "))]
        i = i + 1
    w1 = float(input("w1 []: "))
    w2 = float(input("w2 []: "))#<Só W1 e W2
    b = float(input("b []: "))
    print(x1, x2, d, w1, w2, b)
    arquivo = open("Dados.txt", "w")
    for x in x1:
        arquivo.write(f"{x} ")
    arquivo.write("\n")
    for x in x2:
        arquivo.write(f"{x} ")
    arquivo.write("\n")
    for x in d:
        arquivo.write(f"{x} ")
    arquivo.write("\n")

    arquivo.write(f"{w1} ")
    arquivo.write("\n")
    arquivo.write(f"{w2} ")
    arquivo.write("\n")
    arquivo.write(f"{b} ")
    arquivo.write("\n")

    arquivo.close()


def functionLoad():
    arquivo = open("Dados.txt", "r")
    # Variaveis do result 2
    cache = ""
    terc = 0
    for linha in arquivo:
        print("Print linha:", linha)
        for letra in linha:
            if letra != " " and letra != "\n" and j == 0:  # X1
                x1 = x1 + [int(letra)]
            elif letra != " " and letra != "\n" and j == 1:  # X2
                x2 = x2 + [int(letra)]
            elif letra != " " and letra != "\n" and j == 2:  # D
                d = d + [int(letra)]
            elif j == 3:  # W1
                cache = cache + letra
                if letra != '.':
                    w1 = float(cache)
            elif j == 4:  # W2
                cache = cache + letra
                if letra != '.':
                    w2 = float(cache)
            elif j == 5:  # B
                cache = cache + letra
                if letra != '.':
                    b = float(cache)
            else:
                if settings[0]:
                    print("-Ocorreu um erro-")
                    if letra == " ":
                        print("Erro esperado de leitura: Espaço")
                    elif letra == "\n":
                        print("Erro esperado de leitura: Jump")
        j = j + 1
        terc = 0
        cache = ""
    print("X1:", x1, "X2:", x2, "d:", d, "w1:", w1, "w2:", w2, "B:", b)
    arquivo.close()

'''
 elif j == 5:  # B
    if letra == " ":
        terc = terc + 1
    elif terc == 1 or letra == "\n":
        b = float(cache)
        cache = ""
        cache = cache + letra
        terc = 0
    else:
        cache = cache + letra
'''