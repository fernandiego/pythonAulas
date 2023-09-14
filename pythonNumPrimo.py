# Solicitar ao usuário que insira um número inteiro positivo
try:
    numero = int(input("Digite um número inteiro positivo: "))

    # Verificar se o número é menor ou igual a 1
    if numero <= 1:
        print("Número não é primo.")
    else:
        # Verificar se o número é primo
        is_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                is_primo = False
                break

        if is_primo:
            print(f"{numero} é um número primo.")
        else:
            print(f"{numero} não é um número primo.")

except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro positivo.")
