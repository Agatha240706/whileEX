while True:
    sexo = str(input("Digite seu gênero [M/F]: "))

    if sexo != "N" and sexo != "F":
        print("Escrita errada")
        ini = str(input("Digite seu genêro (M/F): "))
    else:
        break
