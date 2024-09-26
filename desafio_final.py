menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Informe o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor_saque = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite_saque:.2f}.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "4":
        print("Obrigado por usar o sistema bancário. Até logo!")
        break

    else:
        print("Operação inválida! Por favor, selecione uma opção válida.")
