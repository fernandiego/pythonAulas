while True:
    try:
        a = int(input("Entre com um valor numérico: "))
        break
        print(a)
    except ValueError:
        print("Entre com um número válido")
