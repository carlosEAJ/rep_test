num1 =input("Digite o primeiro número: ")
num2 =input("Digite o segundo número: ")

operacao = input("Digite a operação (+, -, *, /): ")
if operacao == "+":
    resultado = float(num1) + float(num2)
    print("Resultado:", resultado)
elif operacao == "-":
    resultado = float(num1) - float(num2)
    print("Resultado:", resultado)
elif operacao == "*":
    resultado = float(num1) * float(num2)
    print("Resultado:", resultado)
elif operacao == "/":
    if float(num2) != 0:
        resultado = float(num1) / float(num2)
        print("Resultado:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")