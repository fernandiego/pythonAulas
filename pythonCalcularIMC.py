# Solicitar ao usuário que insira o peso (em kg) e a altura (em cm)
try:
    peso = float(input("Digite o seu peso em quilogramas (kg): "))
    altura_cm = float(input("Digite a sua altura em centímetros (cm): "))

    # Converter a altura para metros
    altura_m = altura_cm / 100

    # Calcular o IMC
    imc = peso / (altura_m ** 2)

    # Exibir o resultado do IMC
    print(f"Seu Índice de Massa Corporal (IMC) é: {imc:.2f}")

    # Interpretar o resultado do IMC
    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif 18.5 <= imc < 24.9:
        print("Você está com peso saudável.")
    elif 25 <= imc < 29.9:
        print("Você está com sobrepeso.")
    else:
        print("Você está com obesidade.")

except ValueError:
    print("Entrada inválida. Por favor, insira valores numéricos válidos.")
