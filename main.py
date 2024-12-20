from Codes import *

while True:

    functionInitiate()

    print("\n1.IA\n2.\n3.\n4.\n5.Quit")
    result = input("Digite sua escolha: ")
    if result == '1':
        print("\n1.Perceptron\n2.\n3.\n4.\n5.Quit")
        result = input("Digite sua escolha: ")
        if result == '1':
            print("\n1.Create\n2.Set\n3.Get\n4.Run\n5.Settings\n6.Delete")
            result = input("Digite sua escolha: ")
            if result == '1':  # Create
                functionCreate_3D()
                functionCreate_2D_Ds()
                functionCreate_2D_Ws()
                functionCreate_1D()
            elif result == '2':  # Set
                functionSet_3D()
                functionSet_2D_Ds()
                functionSet_2D_Ws()
                functionSet_1D()
            elif result == '3':  # Get
                functionGet()
            elif result == '4':  # Get
                Fairun()
            elif result == '5':  # Configuração
                fuctionSettings()
            elif result == '6':  # Delete
                functionDelete()
    elif result == '5':  # Sair
        quit()
