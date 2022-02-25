"""
17) Faça um algoritmo para ler: a descrição do produto (nome), a
quantidade adquirida e o preço unitário. Calcular e escrever o total
(total = quantidade adquirida * preço unitário), o desconto e o total a
pagar (total a pagar = total - desconto), sabendo-se que:
- Se quantidade <= 5 o desconto será de 2%
- Se quantidade > 5 e quantidade <=10 o desconto será de 3%
- Se quantidade > 10 o desconto será de 5%
"""
# Nome do produto
# Quantidade Adquirida
# Preço unitário do produto
# Preço total adquirido
# Desconto total

nome_produto = input("Informe o nome do produto: ")
valor_produto = int(input("Valor do produto: "))
quantidade = int(input("Quantos você adquiriu: "))
valor_total = quantidade * valor_produto
desconto = 2

if quantidade > 5 <= 10:
    desconto = 3
if quantidade > 10:
    desconto = 5

print(desconto)

valor_desconto = (desconto * valor_total) / 100
valor_final = valor_total - valor_desconto
print("Você recebeu", valor_desconto, "R$ de desconto!")
print("O valor final a se pagar é", valor_final, "R$")
