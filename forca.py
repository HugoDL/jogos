def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "potato"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False


    while (not enforcou and not acertou):

        print("Palavra: ", letras_acertadas)
        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra

            index = index + 1

        letras_faltando = str(letras_acertadas.count("_"))
        print("Ainda faltam acertar {} letras!".format(letras_faltando))

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
