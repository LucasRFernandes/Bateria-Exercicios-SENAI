"""
7) Faça um algoritmo para ler o salário mensal atual de um funcionário e o
percentual de reajuste. Calcular e escrever o valor do novo salário.

"""


salario_mensal = int(input("Digite o salário mensal do funcionario: "))
reajuste = int(input("Digite o porcentual de reajuste (%): "))

resultado_porcentagem = reajuste * salario_mensal / 100
valor_final = salario_mensal + resultado_porcentagem

print(valor_final)
