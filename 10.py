"""
10) Faça um algoritmo que leia dois valores e informe o maior deles.
(Resolvi fazer de uma forma mais diferente em vez de simplesmente fazer
If valor1 > valor2:
    print(valor1)

resolvi fazer de um jeito verificando o resultado da subtração dos valores e seu resultado
"""


valor1 = int(input("Informe o valor 1: "))
valor2 = int(input("Informe o valor 2: "))


if valor1 - valor2 < 0:
    print("O maior valor é", valor2)

if valor2 - valor1 < 0:
    print("O maior valor é", valor1)

if valor1 - valor2 == 0:
    print("Os dois valores são iguais")
