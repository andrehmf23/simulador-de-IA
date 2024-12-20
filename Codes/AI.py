from random import *

# Variavel Global
X1 = []
X2 = []
X3 = []
D1 = []
D2 = []
W1 = []
W2 = []
B = []
Y = 0
A = 0.01
config = [0,0,0]
Teste = 0


def functionTestVoid():

    arquivo = open("Dados.txt", "r")
    global Teste

    for linha in arquivo:
        for letra in linha:
            if letra == "" or letra == "\n" or letra == " ":
                pass
            else:
                Teste = 1
                print(f'letra: {letra}')
    print(Teste)

    arquivo.close()

def functionCreate_3D():

    global X1
    global X2
    global X3

    X3 = []
    i = 0
    j = 0
    k = 0
    while i != config[2]:
        Probabilidademeio = pow(2, config[1])
        Probabilidademeiofixo = pow(2, config[1])
        Conter = 0
        f = 1
        while j != config[1]:
            Probabilidademeiofixo = Probabilidademeiofixo / 2
            Probabilidademeio = Probabilidademeiofixo
            while k != config[0]:
                if Probabilidademeio - 1 != k:
                    X1 = X1 + [Conter]
                else:
                    Probabilidademeio = Probabilidademeio + Probabilidademeiofixo
                    f = -f
                    X1 = X1 + [Conter]
                    if f < 0:
                        Conter = 1
                    else:
                        Conter = 0
                #print(f"Geretor: i: {i}j: {j}k: {k}")
                k = k + 1
            X2 = X2 + [X1]
            X1 = []
            j = j + 1
            k = 0
        X3 = X3 + [X2]
        X2 = []
        i = i + 1
        j = 0
    # Criar outras Questôes->[Aumenta os Xs->[    possibilidades->[0,0,0,1],x2[0,0,0,1],x3[0,0,0,1]]]
    print("X3: ", X3)

def functionCreate_1D():
    i = 0
    global B

    B = []

    while i != config[2]:
        B = B + [round(random(), 2)]
        i = i + 1
    print("B: ", B)

def functionCreate_2D_Ds():
    global D1
    global D2

    i = 0
    j = 0

    #Nova_linha = pow(2, xs)
    #Nova_argumentação = pow(2, Nova_linha)
    D2 = []
    while i != config[2]:
        while j != config[0]:
            D1 = D1 + [randint(0, 1)]
            j = j + 1
        D2 = D2 + [D1]
        D1 = []
        j = 0
        i = i + 1
    print("D2: ", D2)


def functionCreate_2D_Ws():

    global W1
    global W2

    W2 = []
    i = 0
    j = 0
    while i != config[2]:
        while j != config[1]:
            W1 = W1 + [round(random(), 2)]
            j = j + 1
        W2 = W2 + [W1]
        W1 = []
        j = 0
        i = i + 1
    print("W2: ", W2)

def functionSet_3D():

    global X3

    arquivo = open("Dados.txt", "w")
    arquivo.write("x\n")
    for matrix1 in X3:
        for matrix2 in matrix1:
            for matrix3 in matrix2:
                arquivo.write(f'{matrix3} ')
            arquivo.write('\n')
        arquivo.write('_\n')
    arquivo.close()

def functionSet_2D_Ds():

    functionTestVoid()

    global D2

    if Teste == 0:
        print("Informações Faltando...")
    elif Teste == 1:
        arquivo = open("Dados.txt", "a")
        arquivo.write("d\n")
        for matrix1 in D2:
            for matrix2 in matrix1:
                arquivo.write(f'{matrix2} ')
            arquivo.write('\n_\n')
        arquivo.close()

def functionSet_2D_Ws():

    functionTestVoid()

    global W2

    if Teste == 0:
        print("Informações Faltando...")
    elif Teste == 1:
        arquivo = open("Dados.txt", "a")
        arquivo.write("w\n")
        for matrix1 in W2:
            for matrix2 in matrix1:
                arquivo.write(f'{matrix2} ')
            arquivo.write('\n_\n')
        arquivo.close()

def functionSet_1D():
    functionTestVoid()

    global B

    if Teste == 0:
        print("Informações Faltando...")
    elif Teste == 1:
        arquivo = open("Dados.txt", "a")
        arquivo.write("b\n")
        for matrix1 in B:
            arquivo.write(f'{matrix1} ')
            arquivo.write('\n_\n')
        arquivo.close()

def functionGet():
    global X1
    global X2
    global X3
    global D1
    global D2
    global W1
    global W2
    global B

    arquivo = open("Dados.txt", "r")
    for linha in arquivo:
        for letra in linha:
            if letra == 'x':
                X1 = []
                X2 = []
                X3 = []
                i = 0
                for linha in arquivo:
                    for letra in linha:
                        if letra == " " or letra == "\n":
                            pass
                        elif letra == "_":
                            i = i + 1
                            X3 = X3 + [X2]
                            X2 = []
                        else:
                            X1 = X1 + [int(letra)]
                        if i == config[2]:
                            break
                    if X1 == [] and X2 == []:
                        pass
                    else:
                        X2 = X2 + [X1]
                    if i == config[2]:
                        break
                    X1 = []
                print("X3: ", X3)
            elif letra == 'd':
                D1 = []
                D2 = []
                i = 0
                for linha in arquivo:
                    for letra in linha:
                        if letra == " " or letra == "\n":
                            pass
                        elif letra == "_":
                            i = i + 1
                        else:
                            D1 = D1 + [int(letra)]
                        if i == config[2]:
                            break
                    if D1 == []:
                        pass
                    else:
                        D2 = D2 + [D1]
                    if i == config[2]:
                        break
                    D1 = []
                print("D2: ", D2)
            elif letra == 'w':
                W1 = []
                W2 = []
                txt = ""
                i = 0
                for linha in arquivo:
                    for letra in linha:
                        if letra == " ":
                            W1 = W1 + [float(txt)]
                            txt = ""
                        elif letra == "\n":
                            if txt != "":
                                W1 = W1 + [float(txt)]
                            txt = ""
                        elif letra == "_":
                            i = i + 1
                        else:
                            txt = txt + letra
                        if i == config[2]:
                            break
                    if W1 == []:
                        pass
                    else:
                        W2 = W2 + [W1]
                    if i == config[2]:
                        break
                    W1 = []
                print("W2: ", W2)
            elif letra == 'b':
                B = []
                txt = ""
                i = 0
                for linha in arquivo:
                    for letra in linha:
                        if letra == " ":
                            B = B + [float(txt)]
                            txt = ""
                        elif letra == "\n":
                            if txt != "":
                                B = B + [float(txt)]
                            txt = ""
                        elif letra == "_":
                            i = i + 1
                        else:
                            txt = txt + letra
                        if i == config[2]:
                            break
                    if i == config[2]:
                        break
                    txt = ""
                print("B: ", B)



def fuctionSettings():

    global config
    save = []
    i = 0
    arquivo = open("Config.txt", "r")
    for linha in arquivo:
        for letra in linha:
            while i != 10:
                if letra == str(i):
                    save = save + [letra]
                i = i + 1
            i = 0

    while i != len(save):
        if i == 0:
            print(f"Linhas:               {save[i]}")
        elif i == 1:
            print(f"Argumentos:           {save[i]}")
        elif i == 2:
            print(f"Linhas de Raciocínio: {save[i]}")
        elif i == 3:
            print(f"Oculto:               {save[i]}")
        i = i + 1

    arquivo.close()

    verificar = input("Deseja Reconfigurar?")
    if verificar == "Sim" or verificar == "S" or verificar == "s" or verificar == "sim":
        arquivo = open("Config.txt", "w")
        config[0] = int(input("Quantidade de Linhas: "))
        config[1] = int(input("Quantidade de Argumentos: "))
        config[2] = int(input("Quantidade de Linhas de Raciocínio: "))
        config[3] = int(input("Oculto '0' ou '1': "))
        arquivo.write(f'{config[0]}\n')
        arquivo.write(f'{config[1]}\n')
        arquivo.write(f'{config[2]}\n')
        arquivo.write(f'{config[3]}\n')
        arquivo.close()

def fuctionReadConfig():

    global config

    config = []

    getting = ""
    arquivo = open("Config.txt", "r")
    for linha in arquivo:
        for letra in linha:
            if letra == " " or letra == "\n":
                pass
            else:
                getting = getting + letra
        config = config + [int(getting)]
        getting = ""
    arquivo.close()

def Fairun():

    global X3
    global D2
    global W2
    global B
    global A
    global config

    linhas = config[0]
    xs = config[1]
    razao = config[2]

    if X3 != [] or D2 != [] or W2 != [] or B != []:

        i = 0
        j = 0
        k = 0
        v = 0
        Acerto = 0
        Temporary = 0
        while i != razao:
            print("\nPerceptron: ", i + 1)
            print("\ni     x      d         w          b    y  Erro")
            print("______________________________________________")
            while Acerto != linhas:
                Temporary = 0
                X3Temporary = []
                while j != xs:
                    Temporary = Temporary + X3[i][j][k] * W2[i][j]
                    X3Temporary = X3Temporary + [int(X3[i][j][k])]
                    j = j + 1
                Y = Temporary - B[i]

                if Y >= 0:
                    Y = 1
                elif Y < 0:
                    Y = 0
                else:
                    print("Ocorreu um erro grave!")

                Teste = D2[i][k] - Y

                print(v, " ", X3Temporary, " ", D2[i][k], " ", W2[i], " ", B[i], " ", Y, " ", Teste)

                j = 0
                while j != xs:
                    #print(f"Antes: W2: {W2[i][j]}")
                    W2[i][j] = round(W2[i][j] + (A * (Teste) * X3[i][j][k]),4)
                    #print(f"Depois: W2: {W2[i][j]}")
                    j = j + 1
                #print(f"B: {B[i]}")
                B[i] = round(B[i] + (A * (Teste) * -1), 4)
                #print(f"B: {B[i]}")

                if Teste == 0:
                    Acerto = Acerto + 1
                elif Teste == 1 or Teste == -1:
                    Acerto = 0
                else:
                    print("Ocorreu um erro gravissimo!")

                k = k + 1
                v = v + 1
                if k == linhas:
                    k = 0
                j = 0
                if v == 1000:
                    print("Deu ruim!")
                    break
            k = 0
            v = 0
            i = i + 1
            Acerto = 0
    else:
        print("Nenhum parametro salvo detectado!")

def functionDelete():

    global X3, D2, W2, B, config

    if X3 != [] or D2 != [] or W2 != [] or B != []:
        i = 0
        j = 0
        save = []
        Temporary = [X3] + [D2] + [W2] + [B]
        print(Temporary)
        print(Temporary[1])
        print("Total de Linhas de Raciocínio: ", config[2])
        choice = input("Qual linha você deseja destruir?")
        for extrat in Temporary:
            for linha in extrat:
                if str(i) != choice:
                    save = save + [linha]
                i = i + 1
            if j == 0:
                X3 = save
            elif j == 1:
                D2 = save
            elif j == 2:
                W2 = save
            elif j == 3:
                B = save

            i = 0
            save = []
            j = j + 1
        print(X3,"\n",D2,"\n",W2,"\n",B)
        config[2] = config[2] - 1
    else:
        print("Nenhum parametro salvo detectado!")

def functionInitiate():

    global config

    if config[0] == 0 and config[1] == 0 and config[2] == 0:
        fuctionReadConfig()
    else:
        arquivo = open("Config.txt","w")
        arquivo.write(f'{config[0]}\n')
        arquivo.write(f'{config[1]}\n')
        arquivo.write(f'{config[2]}\n')
        arquivo.write(f'{config[3]}\n')
        arquivo.close()