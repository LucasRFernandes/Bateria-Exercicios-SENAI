"""
6) Faça um algoritmo para ler as dimensões de um retângulo (base e
altura), calcular e escrever a área do retângulo.
Obs do aluno: Fiz o código considerando que o usuario vai inserir apenas um valor
inteiro, o programa entende automaticamente que se tratam de centrimetros sem
que o usuario precise digitar isso também!
"""

print("Calculando a área do triangulo em CM")
base = int(input("Informe a Base do retangulo: "))
altura = int(input("Informe a Altura do retangulo: "))
area = base * altura
print("A area do triangulo é igual a", area, "Cm")
