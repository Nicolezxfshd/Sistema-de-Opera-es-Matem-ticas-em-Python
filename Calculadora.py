# Solicite ao usuário que insira dois números para realizar operações matemáticas
def solicitar_numeros():
    while True:
        try:
            num1 = float(input("Insira o primeiro número: "))
            num2 = float(input("Insira o segundo número: "))
            return num1, num2

        # Caso o usuário insira um valor que não seja um número
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")


# Menu usando LIST COMPREHENSION
def menu_operacoes():

    operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]

    print("\nEscolha a operação:")

    # LIST COMPREHENSION
    [print(f"{i+1} - {operacoes[i]}") for i in range(len(operacoes))]

    while True:
        try:
            escolha = int(input("Digite a opção desejada: "))
            if escolha in [1,2,3,4]:
                return escolha
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite apenas números.")


# Utilize lambda para as operações
def realizar_operacao(num1, num2, escolha):

    operacoes = {
        1: lambda x, y: x + y,
        2: lambda x, y: x - y,
        3: lambda x, y: x * y,
        4: lambda x, y: x / y if y != 0 else "Divisão por zero não é permitida"
    }

    return operacoes[escolha](num1, num2)


# Programa principal
def main():

    while True:

        escolha = menu_operacoes()

        # Tratamento especial para divisão por zero
        if escolha == 4:

            while True:

                num1, num2 = solicitar_numeros()

                if num2 != 0:
                    resultado = realizar_operacao(num1, num2, escolha)
                    print(f"Resultado: {resultado}")
                    break

                else:
                    print("Divisor não pode ser zero. Digite novamente.")

        else:

            num1, num2 = solicitar_numeros()
            resultado = realizar_operacao(num1, num2, escolha)
            print(f"Resultado: {resultado}")

        continuar = input("Deseja realizar outra operação? (s/n): ")

        if continuar.lower() != 's':
            print("Encerrando o programa. Obrigado por usar a calculadora!")
            break


main()
