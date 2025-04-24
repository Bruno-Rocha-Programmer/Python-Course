nota1 = nota2 = 0.0
resultado = 0.0

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

resultado = (nota1 + nota2) / 2

if resultado >= 7.0:
    print("Aprovado com média {}".format(resultado))
elif resultado >= 5.0:
    print(f"Recuperação com média {resultado}")
else:
    print("Reprovado com média", resultado)



