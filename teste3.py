def adivinhar_numero():
    # Lista inicial de números psíveis para adivinhar
    numeros_possiveis = [1, 2, 3, 4, 5]
    tentativas = 0
    while True:
        # Gabriel faz um chute
        chute = numeros_possiveis[0] # Pega o primeiro número da lista
        print(f"Gabriel chuta: {chute}")
        # Paulo informa se o chute é maior ou menor que o número a ser adivinhado
        # Para este exemplo, vamos assumir que o número a ser adivinhado é 5
        if chute < 5:
            print("Paulo diz: maior")
            # Gabriel elimina metade dos números psíveis
            numeros_possiveis = numeros_possiveis[len(numeros_possiveis)//2:]
        else:
            print("Paulo diz: menor")
            # Gabriel elimina metade dos números psíveis
            numeros_possiveis = numeros_possiveis[:len(numeros_possiveis)//2]
        tentativas += 1
        # Verifica se Gabriel acertou o número
        if chute == 5:
            print(f"Gabriel acertou o número 5 em {tentativas} tentativas.")
            break
adivinhar_numero()
