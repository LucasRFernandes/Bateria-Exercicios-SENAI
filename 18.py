"""
18) Faça um algoritmo que leia duas notas de avaliação de um aluno.
Calcule a média aritmética das notas. Deverá também ser informado o
percentual de frequência do aluno. Para aprovação, o aluno deverá possuir
a média igual ou superior a 7,0, e o mínimo de frequência de 75%. Exiba na
tela as notas, a média, o percentual e o resultado final.
"""

nota1 = int(input("Nota da primeira prova: "))
nota2 = int(input("Nota da segunda prova: "))
aulas = int(input("Quantas aulas tivemos: "))
faltas = int(input("Quantidade de faltas do Aluno: "))

presencas = aulas - faltas
frequencia = (presencas / aulas) * 100

media = (nota1 + nota2) / 2
if media >= 7:
    if frequencia >= 75:
        print("O aluno foi aprovado!")
        print("Media:", media)
        print("Frequencia", frequencia, "%")

if media < 7:
    if frequencia < 75:
        print("O aluno foi reprovado!")
        print("Media:", media)
        print("Frequencia", frequencia, "%")

if media >= 7:
    if frequencia < 75:
        print("O aluno foi reprovado!")
        print("Media:", media)
        print("Frequencia", frequencia, "%")

if media < 7:
    if frequencia >= 75:
        print("O aluno foi reprovado!")
        print("Media:", media)
        print("Frequencia", frequencia, "%")
