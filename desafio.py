menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

class Lancamento:
    def __init__(self, operacao, valor, saldoDepois):
        self.operacao = operacao
        self.valor = valor
        self.saldoDepois = saldoDepois




class Conta:
    
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    def __init__(self, nome):
        self.titular = nome
        self.saldo = 0
        self.extrato = []
        
    def depositar(self,valor_a_depositar):
        if valor_a_depositar > 0:
            self.saldo += valor_a_depositar
            self.extrato.append(Lancamento("Deposito",valor_a_depositar,self.saldo))
            return 'Depositado com sucesso!'
        return 'Erro: O valor inserido e invalido!'

        
        
    def sacar(self,valorASacar):

        if valorASacar > self.saldo:
            return "Operação falhou! Você não tem saldo suficiente."

        elif valorASacar > self.limite:
            return "Operação falhou! O valor do saque excede o limite."

        elif self.numero_saques >= self.LIMITE_SAQUES:
            return "Operação falhou! Número máximo de saques excedido."

        elif valorASacar > 0:
            self.numero_saques += 1
            self.saldo -= valorASacar
            self.extrato.append(Lancamento("Saque",valorASacar,self.saldo))
            return "Saque realizado com sucesso!"

        else:
            return "Operação falhou! O valor informado é inválido."
                
    def ver_extrato(self):
        extratoMostrado = "------------------------ \n"
        for e in self.extrato:
            extratoMostrado += f"{e.operacao}: R${e.valor:.2f} | Saldo após: R${e.saldoDepois:.2f}\n"
        extratoMostrado += f"\nSaldo atual: R${self.saldo:.2f} \n"
        extratoMostrado += "------------------------ \n"
        return extratoMostrado




class Main:
    def inputParaFloat(self,tipo):
        try:
            return float(input(f"Informe o valor do {tipo}: "))
        except:
            return 0
        
    def run(self):
            
        nome = input("Digite seu nome: ")

        C1 = Conta(nome) 
                    
        while True:
            print(" ")
            opcao = input(menu)

            if opcao == "d":
                valor = self.inputParaFloat("depósito")
                print(C1.depositar(valor))

            elif opcao == "s":
                valor = self.inputParaFloat("saque")

                print(C1.sacar(valor))

            elif opcao == "e":
                print(C1.ver_extrato())

            elif opcao == "q":
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
                
                
programaBancario = Main()
programaBancario.run()