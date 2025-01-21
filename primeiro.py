# criação da variavel do aluno
nome_aluno = " "
#Criação de variaveis para obter  as 4 notas
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
nota4 = 0.0
#Vamos obter o nome do aluno
nome_aluno = input("Digite o nome do aluno: ")
#Vamos obter as notas do aluno
nota1 = float(input("Digite a  primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
#Somar as quatro notas,obter a média e a situação
#>=7 aprovado |<= 4 Reprovado | >4 e <7 Recuperação

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >=7:
    print(f"A média é {media} - Aprovado")
elif media <=4:
    print(f"A média é {media} - Reprovado")
else:
    print(f"A média é {media} - Recuperação")        