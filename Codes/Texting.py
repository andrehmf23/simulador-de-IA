
def arquivodeid():
    arquivo = str(input("Digite o nome do arquivo: "))
    return arquivo

def escrita():
    print("\n1. Escrever\n2. Pular linha\n3.Terminar")
    x = 0
    while x != 3:
        x = int(input("Escolha: "))

        if x == 1:
            arquivo.write(input("->"))
        elif x == 2:
            arquivo.write("\n")
        elif x == 3:
            print("Saindo...")
        else:
            print("\nAconteceu algum errom... Tente novamente!")

while True:
    print("1. Fazer ou refazer um novo arquivo\n2. Reescrever um arquivo\n3. Ler arquivo\n4. Deletar um arquivo\n5. Fechar")
    Central = int(input("Olá o que você gostaria de fazer: "))
    if Central == 1:
        ARQ = arquivodeid()
        arquivo = open(ARQ, "w")
        escrita()
        arquivo.close()

    elif Central == 2:
        ARQ = arquivodeid()
        arquivo = open(ARQ, "a")
        escrita()
        arquivo.close()

    elif Central == 3:
        ARQ = arquivodeid()
        arquivo = open(ARQ, "r")
        print(arquivo)
        print("____________________")
        for linha in arquivo:
            for letra in linha:
                letra = letra.rstrip()
                print(letra)
            linha = linha.rstrip()
            print(linha)
        print("____________________")
        arquivo.close()

    elif Central == 4:
        print("Ainda em desenvolvimento!")

    elif Central == 5:
        print("Fechando...")
        quit()

    else:
        print("\nNada identificado!")
