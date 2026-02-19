print("---------------------------")
print("     CONSULTA DE NOTAS     ")
print("---------------------------")

soma = 0
quantidade = 5

for i in range (1, 6):
    notas = float(input(f"Aluno {i}:"))
    soma += notas

    if notas >= 7:
        print("Aprovado!\n")
    elif notas > 4.5:
        print("Recuperação!\n")
    else:
        print("Reprovado!\n")

media = soma / quantidade
print(f"Média: {media:.2f}")