menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

 => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        deposito = float(input('Digite o valor a ser depositado: '))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == 's':
        sacar = float(input("Informe o valor do saque: "))
        excedeu_saldo = sacar > saldo
        excedeu_limite = sacar > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! o valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif sacar > 0:
            saldo -= sacar
            extrato += f"Saque: R$ {sacar:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == 'e':
        print("\nExtrato")
        print("Não foram Realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")

    elif opcao == 'q':
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
