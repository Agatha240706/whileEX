pares = 0

while True:
    num = int(input("Digite um número: "))
    if num == 0:
        print("Você digitou [0], parou o programa.")
        print("A soma dos números pares é: ", pares)
        break
    elif num %2 == 0:
        pares += num
        f = str(input("Deseja continuar?(S/N): "))

        if f.upper() == "N":
            print("A soma dos números pares é: ", pares)
            break