"""
14) Faça um algoritmo que leia o salário fixo e o valor das vendas
efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma
comissão de 3% sobre o total das vendas até R$ 1.500,00, mais 5% sobre o
que ultrapassar este valor, calcular e escrever o seu salário total.
"""

# O VENDEDOR TEM UM SALARIO FIXO
# ELE FAZ VENDAS QUE NO FINAL SÃO SOMADAS
# SE O VALOR DAS VENDAS FOR IGUAL A 1500 ELE RECEBE 3% DE COMISSÃO DE 1500
# SE O VALOR FOR SUPERIOR A 1500 ELE RECEBE 5% DE COMISSÃO
# O VALOR DA COMISSÃO TEM QUE SER SOMADO AO VALOR TOTAL QUE ELE RECEBE


salario = int(input("Informe o salario fixo do trabalhador: "))
vendastotais = int(
    input("Informe o valor total das vendas do mês do funcionario: ")
)
valorcomissao = 0
if vendastotais <= 1500:
    valorcomissao = 3
else:
    valorcomissao = 5

reajuste = valorcomissao * vendastotais / 100


salario_final = salario + reajuste


print("O salário final do funcionario será de:", salario_final)
