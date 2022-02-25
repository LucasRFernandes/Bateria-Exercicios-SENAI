"""
12) Faça um algoritmo que leia um valor inteiro e informe se é par ou
ímpar.
"""


valor = int(input("Informe um valor: "))

valordividido = valor / 2
valordividido_str = str(valordividido)


if valordividido_str[-1] == '0':
    print(valor, "é par")

else:
    print(valor, "é impar")
