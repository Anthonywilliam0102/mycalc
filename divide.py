def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro! Divisão por zero."

if __name__ == "__main__":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"A divisão é: {divisao(num1, num2)}")

