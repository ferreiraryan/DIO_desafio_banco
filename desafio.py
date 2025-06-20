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


class lancamento:
    def __init__(self, operacao, valor,data,saldoDepois):
        self.operacao = operacao
        self.valor = valor
        # self.data = data
        self.saldoDepois = saldoDepois




class conta:
    
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    def __init__(self, nome):
        self.titular = nome
        self.saldo = 0
        self.extrato = []
        
    def depoitar(self,valorADepositar):
        if valorADepositar > 0:
            self.saldo += valorADepositar
            self.extrato.append(lancamento("Deposito",valorADepositar,self.saldo))
            return 'Depositado com sucesso!'
        return 'Erro: O valor inserido e invalido!'

        
        
    def sacar(self,valorASacar):

        if valorASacar > self.saldo:
            return "Operação falhou! Você não tem saldo suficiente."

        elif valorASacar > self.limite:
            return "Operação falhou! O valor do saque excede o limite."

        elif self.numero_saques > LIMITE_SAQUES:
            return "Operação falhou! Número máximo de saques excedido."

        elif valor > 0:
            self.saldo -= valorASacar
            self.extrato.append(lancamento("Saque",valorASacar,self.saldo))
            self.numero_saques += 1

        else:
            return "Operação falhou! O valor informado é inválido."
            
        
        
            
            
            
            
        





while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")