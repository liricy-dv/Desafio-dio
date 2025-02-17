menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.00
limite = 800.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 4

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Insira o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo suficiente.")

        elif excedeu_limite:
            print("O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione uma das opções")
