menu = '''

[d] depositar
[s] sacar
[e] extrato
[q] sair

>: '''

balance = 0
LIMITE_WITHDRAW = 500
bank_statement = ''
withdraw_number = 0
LIMIT_NUMBER_WITHDRAW = 3

while True:
    op = input(menu)
    
    if op == 'd':
        print("-----Deposito-----")
        value = float(input("Informe o valor de depósito: "))

        if value > 0:
            balance += value  
            bank_statement += f"Depósito de {value:.2f} R$." 

        else:
            print('Operação falhou.')
    elif op == 's':
        print('-----Saque-----')
        value = float(input("informe o valor de saque: "))

        exceeded_balance = value > balance
        exceeded_limit = value > LIMITE_WITHDRAW
        exceeded_withdrawals =  withdraw_number >= LIMIT_NUMBER_WITHDRAW

        if exceeded_balance:
            print("Você não tem saldo suficiente.")
        elif exceeded_limit:
            print("Você não pode sacar mais que 500 reais.")
        elif exceeded_withdrawals:
            print("Limite de saques atingido.")
        elif value > 0:
            balance -= value
            bank_statement += f"Saque de {value:.2f} R$ realizado."
            withdraw_number += 1

        else:
            print("Valor informado inválido.")
    elif op == "e":
        print("------Extrato-----")
        print("não foram realizadas operações bancárias." if not bank_statement else bank_statement)
        print(f"saldo: {balance} R$")
        print("--------------------")   
    elif op == "q":
        break

    else:
        print("Operação Invalida")