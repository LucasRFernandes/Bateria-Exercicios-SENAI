"""
13) Faça um algoritmo que leia as notas de duas avaliações de um aluno.
Calcule a média aritmética e escrever uma mensagem que informe se o aluno
foi ou não aprovado (considerar aprovado com a média igual ou maior que
7,0). Escrever também a média calculada.
"""


nota1 = int(input("Nota da primeira prova: "))
nota2 = int(input("Nota da segunda prova: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("A media do aluno foi", media)
    print("O aluno está aprovado")
else:
    print("A media do aluno foi", media)
    print("O aluno está reprovado")
