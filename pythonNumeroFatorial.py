def calcular_fatorial(n):
    if n < 0:
        return "Não é possível calcular o fatorial de um número negativo."
    elif n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, n + 1):
            fatorial *= i
        return fatorial

# Solicitar ao usuário que insira um número
try:
    numero = int(input("Digite um número não negativo para calcular o fatorial: "))
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro não negativo.")
