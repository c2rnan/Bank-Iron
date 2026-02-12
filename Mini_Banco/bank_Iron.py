banco = {}

def criar_conta(banco):
    numero_conta = len(banco) + 1
    titular = input("Quem e o titular da conta? ")

    banco[numero_conta] = {
        "Titular": titular,
        "Saldo": 0.00,
        "Historico": []
    }

    print(f"Conta {numero_conta} criado com Sucesso!")

def depositar(banco):
    numero_conta = int(input("Digite o numero da conta que deseja depositar: "))

    if numero_conta in banco:
        valor = float(input("Valor que deseja depositar: "))

        if valor > 0:
            banco[numero_conta]['Saldo'] += valor
            banco[numero_conta]['Historico'].append(f"Deposito: +{valor:.2f}")
            print(f"Deposito feito com Sucesso! Saldo atual: {banco[numero_conta]['Saldo']:.2f}")
        else:
            print("Valor inválido!")
    else: 
        print("Conta não encontrada!")


def sacar(banco):
    numero_conta = int(input("Digite o numero da conta que deseja sacar: "))

    if numero_conta in banco:
        valor = float(input("Valor que deseja sacar: "))

        if valor <= 0:
            print("Valor inválido!")
        elif valor > banco[numero_conta]['Saldo']:
            print("Saldo insuficiente!")
        else:
            banco[numero_conta]['Saldo'] -= valor
            banco[numero_conta]['Historico'].append(f"Saque: -{valor:.2f}")
            print(f"Saque feito com sucesso! Saldo atual: {banco[numero_conta]['Saldo']:.2f}")


    else: 
        print("Conta não encontrada!")

def ver_saldo(banco):
    numero_conta = int(input("Digite o numero da conta que deseja visualizar: "))

    if numero_conta in banco:
        print(f"Saldo: {banco[numero_conta]['Saldo']:.2f}")
    else:
        print("Conta não encontrada!")

def historico(banco):
    numero_conta = int(input("Digite o numero da conta que deseja visualizar o historico: "))

    if numero_conta in banco:
        historico = banco[numero_conta]['Historico']
        
        if historico:
            print("-----------------------------\n")
            print("      H I S T O R I C O      \n")
            print("-----------------------------\n")
            for movimentacao in historico:
                print(movimentacao)
            print()
        else:
            print("Nenhuma movimentação registrada.\n")
    else:
        print("Conta não encontrada!\n")
        
def menu():
    print("===== BANCO IRON =====")
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver Saldo")
    print("5 - Ver Historico")
    print("6 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção:\n")

    if opcao == "1":
        criar_conta(banco)
       
    elif opcao == "2":
        depositar(banco)
       
    elif opcao == "3":
        sacar(banco)

    elif opcao == "4":
        ver_saldo(banco)
       
    elif opcao == "5":
        historico(banco)
       
    elif opcao == "6":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!\n")