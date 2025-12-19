class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor} realizado. Saldo atual: R${self.saldo}")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
        else:
            print("Saldo insuficiente")
    
# Teste
conta = ContaBancaria("Felipe")

valor_deposito = float(input("Digite o valor para depósito: R$ "))
conta.depositar(valor_deposito)

valor_saque = float(input("Digite o valor para saque: R$ "))
conta.sacar(valor_saque)
