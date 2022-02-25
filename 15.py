"""
15) Faça um algoritmo que leia: número da conta do cliente, saldo, débito
e crédito. Posteriormente, calcular e escrever o saldo atual (saldo atual
= saldo - débito + crédito). Se saldo atual for maior ou igual a zero
informar com a mensagem “Saldo Positivo”, senão, “Saldo Negativo”.
"""


numero_conta = int(input("Informe o número da conta: "))
saldo = int(input("Informe o Saldo da conta: "))
debito = int(input("Informe o débito da conta: "))
credito = int(input("Informe o crédito da conta: "))


saldo_atual = saldo - debito + credito
print("Seu saldo atual é de", saldo_atual, "R$")
if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")
