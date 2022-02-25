"""
8) Uma revendedora de carros usados paga a seus funcionários vendedores um
salário fixo por mês, mais uma comissão também fixa para cada carro
vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um
algoritmo que leia o número de carros por ele vendidos, o valor total de
suas vendas, o salário fixo e o valor que ele recebe por carro vendido.
Calcule e escreva o salário final do vendedor.

Ler carros vendidos
valor total dos carros vendidos
salario fixo do vendedor
quanto ele recebe por carro vendido
dizer salario mensal
"""


salario_fixo = int(input("Salario fixo do vendedor: "))
comissao_fixa = int(
    input("Quanto ele recebe a mais por \nCada carro vendido?: ")
)
carros_vendidos = int(input("Quantos carros ele vendeu no mês: "))


salario_final = salario_fixo + (carros_vendidos * comissao_fixa)
print("O trabalhador deve receber", salario_final, "R$ nesse mês.")
