numero1 = int(input('Informe o número de Processos: '))
numero2 = int(input('Informe o número de Juízes: '))

if numero2 != 0:
    resultado = numero1 / numero2
    print("Há", resultado, "processos a serem julgados por cada Juiz")
else:
    print("Não é possível divisão por zero")
